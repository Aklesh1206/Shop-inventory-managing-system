# Shop Inventory Management System
A shop inventory management system is software designed to track and control the flow of goods in a business, from purchasing and storage to sales and fulfillment. It centralizes and automates records of inventory, enabling businesses to see accurate stock levels, streamline reordering, minimize errors, and optimize order fulfillment.

# Features
- Add, edit, and delete products (name, price, quantity, etc.).
- Track current stock levels and update quantities after purchases or restocking.
- Search and filter products by name, category, or ID.
- Store data in a local database (SQLite) for persistance.
- User-friendly Tkinter GUI with buttons, tables, and dialog windows.

## Tech Stack
- **Language:** Python 3.6
- **GUI Framework:** Tkinter 
- **Database:** SQLite
- **Storage** JSON file format
- **Libraries Used:**
- `ttk` for styled widgets  
- `sqlite3` for database access

<img width="413" height="93" alt="Screenshot 2025-11-23 211007" src="https://github.com/user-attachments/assets/fc627932-5d39-4ab5-bb46-458417cb1b86" />


<img width="1048" height="790" alt="Screenshot 2025-11-23 152458" src="https://github.com/user-attachments/assets/4d444783-59ff-4cb2-ae95-1a667ccefe35" />

  
## Installation and Running
**Clone the repository**

1.Make sure Python 3.6+
2.Verify tkinter: python -m tkinter
3.Download sims.py
4.Run: python pythonMini_project.py
5.The app stores data in SQLite database.

## Usage
1. Initialize the database 
2. Run the application
3. Basic workflow:
- Open the app  
- Use **Add Product** to insert new items with name, price, and initial stock. (eg= Mango juice, price=20, Stock=45)
- Use **Edit** or **Delete** to maintain product records as needed.(Like you can change the price, stock, name or serial number)
- Use **Search** to quickly find items by keyword. (you can use this to find items saved)

<img width="1049" height="790" alt="Screenshot 2025-11-23 212444" src="https://github.com/user-attachments/assets/edd0eaa4-6bf0-4d23-b9cc-2df6fa80b6e8" />







