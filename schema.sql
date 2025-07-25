CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Year INTEGER,
    Quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Members (
    MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    MemberID INTEGER,
    BookID INTEGER,
    IssueDate DATE,
    ReturnDate DATE,
    FOREIGN KEY(MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY(BookID) REFERENCES Books(BookID)
);
