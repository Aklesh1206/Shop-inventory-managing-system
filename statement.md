# Shop Inventory Management System(SIMS)

## Problem Statement
Traditional inventory management methods in small and medium-sized retail shops rely heavily on manual record-keeping, which is inefficient, error-prone, and time-consuming. Storekeepers often struggle to keep stock data updated, produce timely and accurate reports, and prevent stockouts or overstocking due to the lack of real-time inventory tracking. Manual processes make it difficult to manage stock across multiple locations, maintain data integrity, and secure inventory information from unauthorized access. These challenges result in lost sales, excess inventory costs, inaccurate forecasting, delayed decision-making, and an overall reduction in operational efficiency.​

## Scope of the Project
The project focuses on building a standalone desktop application for managing a single shop’s inventory. It will allow the user to maintain a product catalog, record stock levels, and update quantities after purchases and sales. The system will provide a graphical user interface (GUI) for daily operations such as adding a new product, editing an existing product, and viewing current stock. Data will be stored locally (SQLite), and the initial scope will not cover multi‑branch operations, advanced analytics, or online access. However, the design will be kept modular so that features like reporting, alerts, or user roles can be added later if required.

## Target Users
- Small shop owners who need a simple way to keep track  their products and stock levels.
- Store managers or staff responsible for updating inventory and handling billing at the counter.
- Students or beginners learning software development who want a practical example of a CRUD‑based desktop application with a GUI.
- Micro and small businesses that do not have the budget or need for complex enterprise resource planning (ERP) systems but still want to reduce errors and save time.

## High-Level Features
- Product Management  
  - Add new products with details such as name, category, price, and initial quantity.  
  - Edit or delete existing products when information changes or items are discontinued.

- Inventory Tracking  
  - View a list of all products with current stock levels.  
  - Automatically update stock when items are sold or restocked.  
  - Search and filter products by name, category, or ID.

- Data Storage and Basic Validation  
  - Store product and transaction data in a local storage mechanism (SQLite).  
  - Perform basic input validation (e.g., prevent negative quantities, ensure required fields are filled).

- Usability and User Interface  
  - Provide a Tkinter‑based GUI with clear buttons and forms for common tasks.  
  - Display messages or dialogs for success, errors, and confirmations.

- Extensibility (Future Enhancements)  
  - Support for low‑stock alerts and simple inventory reports.  
  - User authentication (e.g., admin and staff roles).  
  - Export data to CSV/Excel for backup or external analysis.
