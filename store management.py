from tkinter import *
from employee import employeeclass
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Inventory Management System")
        self.root.geometry("1200x600+0+0")
       # Title
        self.title = Label(self.root,
                           text="Store Inventory Management System",
                           font=("times new roman", 35, "bold"),
                           bg="sky blue",
                           fg="Black" ,
                           anchor="center")
                        
        self.title.place(x=0, y=0, relwidth=1, height=60)
        #Logout Button
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=1050,y=10,height=40,width=100)
        #Clock
        self.lbl_clock = Label(
            self.root,
            text=" Namaste, Welcome to Store Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15,),
            bg="lightyellow",
            fg="black",
            anchor="center")
        self.lbl_clock.place(x=0, y=60, relwidth=1, height=30)
    
        #Menu
    
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white") 
        LeftMenu.place(x=0, y=90, width=200, height=510)          
            #Menu Label
        lbl_menu = Label(
            LeftMenu,
            text="Menu",font=("times new roman", 20, "bold"),
            bg="Green",cursor="hand2").pack(side=TOP, fill=X)
        btn_employee = Button(
            LeftMenu,
            text="Employee",font=("times new roman", 20, "bold"),
            bg="White",cursor="hand2").pack(side=TOP, fill=X)
        btn_Category = Button(
            LeftMenu,
            text="Category",font=("times new roman", 20, "bold"),
            bg="White",cursor="hand2").pack(side=TOP, fill=X)
        btn_Products = Button(
            LeftMenu,
            text="Products",font=("times new roman", 20, "bold"),
            bg="White",cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(
            LeftMenu,
            text="Exit",font=("times new roman", 20, "bold"),
            bg="White",cursor="hand2").pack(side=TOP, fill=X)
    
        #Footer
        lbl_footer = Label(
            self.root,
            text="SIMS - Store Inventory Management System | Developed By Aklesh",
            font=("times new roman", 12,),
            bg="Dark grey",
            fg="black",
            anchor="center").pack(side=BOTTOM, fill=X)
        self.lbl_Employee = Label(
            self.root,
            text=" Total Employee\n[ 0 ]",
            font=("Goudy old Time", 15,),
            bg="lightblue",
            fg="black",
            anchor="center")
        self.lbl_Employee.place(x=300, y=120, height=150,)
        self.lbl_Category = Label(
            self.root,
            text=" Total Category\n[ 0 ]",
            font=("Goudy old Time", 15,),
            bg="lightyellow",
            fg="black",
            anchor="center")
        self.lbl_Category.place(x=1000, y=120, height=150,)
        self.lbl_Products = Label(
            self.root,
            text=" Total Products\n[ 0 ]",
            font=("Goudy old Time", 15,),
            bg="lightpink",
            fg="black",
            anchor="center")
        self.lbl_Products.place(x=650, y=120, height=150,)
        
        #===============================================================================================================
        def employee():
            self.new_win = Toplevel(self.root)
            self.new_obj = employeeclass(self.new_win)
    
    
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()

