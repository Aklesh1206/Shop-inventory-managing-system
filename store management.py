import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

 # DATABASE PART 

def connect_db():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qty INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    return conn, cur

conn, cur = connect_db()

#  MAIN APP CLASS 

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Inventory Management System | Created by Aklesh")
        self.root.geometry("700x500+200+100")
        self.root.resizable(False, False)

        # VARIABLES 
        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_qty = tk.StringVar()
        self.var_price = tk.StringVar()

        #  TOP FRAME 
        top_frame = tk.LabelFrame(self.root, text="Item Details", padx=10, pady=10)
        top_frame.pack(fill="x", padx=10, pady=5)

        # ID 
        tk.Label(top_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_id = tk.Entry(top_frame, textvariable=self.var_id, state="readonly", width=10)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Name
        tk.Label(top_frame, text="Name").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_name = tk.Entry(top_frame,bg="light yellow", textvariable=self.var_name, width=20)
        self.entry_name.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Quantity
        tk.Label(top_frame, text="Quantity").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_qty = tk.Entry(top_frame,bg="light yellow", textvariable=self.var_qty, width=10)
        self.entry_qty.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Price
        tk.Label(top_frame, text="Price").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_price = tk.Entry(top_frame,bg="light yellow", textvariable=self.var_price, width=10)
        self.entry_price.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        #  BUTTONS
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="Add", width=10, command=self.add_item,bg="light green").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=10, command=self.update_item).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=10, command=self.delete_item,bg="red").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Clear", width=10, command=self.clear_fields).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Refresh", width=10, command=self.fetch_items).grid(row=0, column=4, padx=5)

        #  TABLE 
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        scroll_y = tk.Scrollbar(table_frame, orient="vertical")
        scroll_y.pack(side="right", fill="y")

        self.item_table = ttk.Treeview(
            table_frame,
            columns=("id", "name", "qty", "price"),
            yscrollcommand=scroll_y.set,
            show="headings"
        )
        scroll_y.config(command=self.item_table.yview)

        self.item_table.heading("id", text="ID")
        self.item_table.heading("name", text="Name")
        self.item_table.heading("qty", text="Quantity")
        self.item_table.heading("price", text="Price")

        self.item_table.column("id", width=50, anchor="center")
        self.item_table.column("name", width=250)
        self.item_table.column("qty", width=80, anchor="center")
        self.item_table.column("price", width=80, anchor="center")

        self.item_table.pack(fill="both", expand=True)
        self.item_table.bind("<ButtonRelease-1>", self.get_selected_row)

        # Load data at start
        self.fetch_items()

    # HELPER FUNCTIONS 

    def clear_fields(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_qty.set("")
        self.var_price.set("")

    def validate_fields(self, need_id=False):
        if need_id and self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a record from table first.")
            return False

        if self.var_name.get().strip() == "" or self.var_qty.get().strip() == "" or self.var_price.get().strip() == "":
            messagebox.showerror("Error", "Name, Quantity and Price are required.")
            return False

        # Quantity integer check
        try:
            int(self.var_qty.get())
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer.")
            return False

        # Price float check
        try:
            float(self.var_price.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number.")
            return False

        return True

    # DB OPERATIONS 

    def add_item(self):
        if not self.validate_fields(need_id=False):
            return

        name = self.var_name.get().strip()
        qty = int(self.var_qty.get())
        price = float(self.var_price.get())

        try:
            cur.execute("INSERT INTO items (name, qty, price) VALUES (?, ?, ?)", (name, qty, price))
            conn.commit()
            messagebox.showinfo("Success", "Item added successfully.")
            self.fetch_items()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error while adding item: {e}")

    def fetch_items(self):
        self.item_table.delete(*self.item_table.get_children())
        cur.execute("SELECT * FROM items")
        rows = cur.fetchall()
        for row in rows:
            self.item_table.insert("", "end", values=row)

    def get_selected_row(self, event):
        selected = self.item_table.focus()
        if selected == "":
            return
        data = self.item_table.item(selected, "values")
        # data -> (id, name, qty, price)
        self.var_id.set(data[0])
        self.var_name.set(data[1])
        self.var_qty.set(data[2])
        self.var_price.set(data[3])

    def update_item(self):
        if not self.validate_fields(need_id=True):
            return

        item_id = self.var_id.get()
        name = self.var_name.get().strip()
        qty = int(self.var_qty.get())
        price = float(self.var_price.get())

        try:
            cur.execute("UPDATE items SET name=?, qty=?, price=? WHERE id=?", (name, qty, price, item_id))
            conn.commit()
            messagebox.showinfo("Success", "Item updated successfully.")
            self.fetch_items()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error while updating item: {e}")

    def delete_item(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this item?")
        if not confirm:
            return

        try:
            cur.execute("DELETE FROM items WHERE id=?", (self.var_id.get(),))
            conn.commit()
            messagebox.showinfo("Deleted", "Item deleted successfully.")
            self.fetch_items()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error while deleting item: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)

    root.mainloop()
