import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ---------------- #
conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    status TEXT
)
''')

conn.commit()

# ---------------- LOGIN ---------------- #
USERNAME = "admin"
PASSWORD = "1234"

# ---------------- FUNCTIONS ---------------- #
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def add_book():
    book = book_entry.get()

    if book:
        cur.execute(
            "INSERT INTO books(name, status) VALUES(?, ?)",
            (book, "Available")
        )
        conn.commit()

        messagebox.showinfo("Success", "Book Added Successfully")

        book_entry.delete(0, tk.END)
        view_books()


def view_books():
    listbox.delete(0, tk.END)

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    for row in rows:
        listbox.insert(
            tk.END,
            f"{row[0]} | {row[1]} | {row[2]}"
        )


def issue_book():
    selected = listbox.get(tk.ACTIVE)

    if selected:
        book_id = selected.split('|')[0].strip()

        cur.execute(
            "UPDATE books SET status='Issued' WHERE id=?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Book Issued")

        view_books()


def return_book():
    selected = listbox.get(tk.ACTIVE)

    if selected:
        book_id = selected.split('|')[0].strip()

        cur.execute(
            "UPDATE books SET status='Available' WHERE id=?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Book Returned")

        view_books()


def delete_book():
    selected = listbox.get(tk.ACTIVE)

    if selected:
        book_id = selected.split('|')[0].strip()

        cur.execute(
            "DELETE FROM books WHERE id=?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Book Deleted")

        view_books()


# ---------------- MAIN WINDOW ---------------- #
def open_main_window():

    global root
    global book_entry
    global listbox

    root = tk.Tk()

    root.title("Book Management System")
    root.geometry("600x500")

    title = tk.Label(
        root,
        text="Book Management System",
        font=("Arial", 20, "bold")
    )

    title.pack(pady=10)

    book_entry = tk.Entry(
        root,
        width=40,
        font=("Arial", 12)
    )

    book_entry.pack(pady=10)

    add_btn = tk.Button(
        root,
        text="Add Book",
        width=20,
        command=add_book
    )

    add_btn.pack(pady=5)

    view_btn = tk.Button(
        root,
        text="View Books",
        width=20,
        command=view_books
    )

    view_btn.pack(pady=5)

    issue_btn = tk.Button(
        root,
        text="Issue Book",
        width=20,
        command=issue_book
    )

    issue_btn.pack(pady=5)

    return_btn = tk.Button(
        root,
        text="Return Book",
        width=20,
        command=return_book
    )

    return_btn.pack(pady=5)

    delete_btn = tk.Button(
        root,
        text="Delete Book",
        width=20,
        command=delete_book
    )

    delete_btn.pack(pady=5)

    listbox = tk.Listbox(
        root,
        width=70,
        height=15
    )

    listbox.pack(pady=10)

    view_books()

    root.mainloop()


# ---------------- LOGIN WINDOW ---------------- #
login_window = tk.Tk()

login_window.title("Login")
login_window.geometry("300x250")

heading = tk.Label(
    login_window,
    text="Library Login",
    font=("Arial", 16, "bold")
)

heading.pack(pady=10)

username_label = tk.Label(
    login_window,
    text="Username"
)

username_label.pack()

username_entry = tk.Entry(login_window)

username_entry.pack(pady=5)

password_label = tk.Label(
    login_window,
    text="Password"
)

password_label.pack()

password_entry = tk.Entry(
    login_window,
    show='*'
)

password_entry.pack(pady=5)

login_btn = tk.Button(
    login_window,
    text="Login",
    width=15,
    command=login
)

login_btn.pack(pady=20)

login_window.mainloop()