# 🏥 Hospital Management System (Tkinter & MySQL)

This project is a simple **Hospital Management System** developed using **Python's Tkinter** for the graphical user interface and **MySQL** for data persistence. It allows users to input, view, generate prescriptions, update, and delete patient and medication records.

---
## 🌟 Architectural Overview

The application follows a **Two-Tier Architecture**:

### Client Tier (Presentation & Logic)
Handled by the **Python application** using the `tkinter` library.

* **GUI:** The `Hospital` class manages all GUI elements (frames, labels, entry fields, buttons, and the Treeview for data display).
* **Application Logic:** Methods like `generate_prescription`, `clear_fields`, `on_row_selected`, and data validation are handled here.

### Data Tier (Database)
Handled by the **MySQL server**.

* **Database Connection:** The `mysql.connector` library establishes communication.
* **Data Persistence:** The application interacts with the `hospital_data` database and the `data` table to perform **CRUD** (Create, Read, Update, Delete) operations via SQL queries (`INSERT`, `SELECT`, `UPDATE`, `DELETE`).

---

### 🧱 Key Components

| Component | Technology | Role |
| :--- | :--- | :--- |
| **GUI** | `tkinter`, `ttk` | User interface design and event handling. |
| **Database Connector** | `mysql.connector` | Connects the Python application to the MySQL server. |
| **Hospital Class** | Python OOP | The core class managing UI layout, Tkinter variables, business logic, and database operations. |
| **hospital\_data** | MySQL Database | Stores all patient and prescription records. |

---
## 🛠️ Step-by-Step Setup Guide

Follow these steps to set up and run the project locally.

### Step 1: Prerequisites

Ensure you have the following installed on your system:

* **Python 3.x**
* **MySQL Server** (e.g., via XAMPP, MySQL Workbench, or a standalone installation)

### Step 2: Install Python Dependencies

You need the **MySQL Connector for Python** to interact with the database.

Open your terminal or command prompt and run:

```bash
pip install mysql-connector-python
