# Advanced Book Management System

## Overview

The **Advanced Book Management System** is a desktop application developed using **Python, Tkinter, and SQLite3**. It provides a simple graphical interface for managing books, users, and book transactions.

The system supports authentication, book management, issuing and returning books, and persistent database storage.

## Features

* 🔐 **Login Authentication** – Secure user login system
* ➕ **Add Books** – Add new books to the library
* 📚 **View Books** – Display available books and their details
* 🗑️ **Delete Books** – Remove books from the database
* 📖 **Issue Books** – Issue books to users
* 🔄 **Return Books** – Return previously issued books
* 💾 **SQLite Database** – Store and manage application data
* 🖥️ **Tkinter GUI** – User-friendly graphical interface
* 📁 **File Handling** – Manage application-related files and data

## Technologies Used

* **Python**
* **Tkinter**
* **SQLite3**

## Project Structure

```text
Advanced-Book-Management-System/
│
├── main.py
├── README.md
└── database/
    └── library.db
```

> The exact project structure may vary depending on the implementation.

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Advanced-Book-Management-System
```

### 2. Run the Application

```bash
python main.py
```

If your system uses the Python launcher:

```bash
py main.py
```

## Database

The application uses **SQLite3** for persistent data storage. SQLite is lightweight and does not require a separate database server.

## Application Workflow

1. Launch the application.
2. Log in using valid credentials.
3. Add or view books.
4. Issue books to users.
5. Return issued books when required.
6. Delete books when they are no longer needed.
7. All relevant information is stored in the SQLite database.

## Future Enhancements

Possible future improvements include:

* Search and filter books
* User registration
* Due-date and fine calculation
* Book availability tracking
* Admin dashboard
* Improved authentication and authorization
* Export library records to CSV/PDF

## Author

Developed as a Python-based database management project using Tkinter and SQLite3.
