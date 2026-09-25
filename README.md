# 🏦 Banking System - Mini Project

A simple **menu-driven Python banking application** that simulates real-world banking operations like account creation, secure login, deposits, withdrawals, transfers, and transaction history tracking.

This project was built as a mini project to combine core Python concepts into one functional, real-world application.

---

## ✨ Features

- 🆕 **Create Account** – Enter name, phone number & create a PIN
- 🔐 **Login** – Access your account using Account Number & PIN
- 💰 **Check Balance** – View your current account balance
- ➕ **Deposit Money** – Add funds to your account
- ➖ **Withdraw Money** – Withdraw funds (with balance check)
- 🔁 **Transfer Money** – Send money to another account instantly
- 📜 **Transaction History** – View all deposits, withdrawals & transfers
- 🔑 **Change PIN** – Update your PIN securely
- 🚪 **Logout** – End session and return to the main menu

---

## 🛠️ Python Concepts Used

| Concept | Where it's used |
|---|---|
| Variables & Data Types | Storing account details, balances, PINs |
| Conditional Statements | Validating login, balance checks, input checks |
| Loops | Menu navigation (`while True` loops) |
| Functions | Each banking feature is a separate function |
| Lists & Dictionaries | Storing accounts and transaction history |
| String Operations | Formatting names, messages, timestamps |
| Modules | `random` for account numbers, `datetime` for timestamps |

---

## 📂 Project Structure

```
CREATE ACCOUNT
      ↓
Account Number + PIN
      ↓
    LOGIN
      ↓
┌─────────────────────────┐
│      ACCOUNT MENU       │
├─────────────────────────┤
│ 1. Check Balance        │
│ 2. Deposit              │
│ 3. Withdraw             │
│ 4. Transfer             │
│ 5. Transaction History  │
│ 6. Change PIN           │
│ 7. Logout               │
└─────────────────────────┘
      ↓
    LOGOUT
      ↓
  MAIN MENU
```

---

## 🚀 How to Run

1. Make sure **Python 3** is installed on your system.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python banking_system.py
```

5. Follow the on-screen menu to create an account, log in, and perform banking operations.

> ⚠️ Note: This project stores data **in memory only** (using Python dictionaries). All accounts and transactions reset when the program is closed, since no database or file storage is used — as per the mini project's scope.

---

## 📸 Sample Menu

```
=============================================
           WELCOME TO PYTHON BANK
=============================================
1. Create Account
2. Login
3. Exit
```

---

## 🎯 Project Objective

The main objective of this project is to combine the Python concepts learned so far into one real-world application, and to understand how individual concepts (variables, loops, functions, dictionaries, modules) work together to build a functional system.

## 🌍 Real-World Connection

This project demonstrates how programming concepts can be used to model a simplified version of real banking applications — including account management, transactions, authentication, and transaction records.

---

## 👤 Author

Add your name here before submitting:

**Name:** _Your Name_
**Project:** Banking System – Mini Project
**Submission Deadline:** 25th September

---

## 📄 License

This project is created for educational purposes as part of a mini project assignment.
