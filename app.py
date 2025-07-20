import sqlite3
from datetime import datetime

conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

def add_book(title, author, year, quantity):
    cursor.execute("INSERT INTO Books (Title, Author, Year, Quantity) VALUES (?, ?, ?, ?)",
                   (title, author, year, quantity))
    conn.commit()
    print("✅ Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM Books")
    for row in cursor.fetchall():
        print(row)

def add_member(name, email):
    cursor.execute("INSERT INTO Members (Name, Email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("✅ Member registered!")

def issue_book(member_id, book_id):
    issue_date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO Transactions (MemberID, BookID, IssueDate) VALUES (?, ?, ?)",
                   (member_id, book_id, issue_date))
    conn.commit()
    print("✅ Book issued!")

def return_book(transaction_id):
    return_date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("UPDATE Transactions SET ReturnDate = ? WHERE TransactionID = ?", (return_date, transaction_id))
    conn.commit()
    print("✅ Book returned!")
