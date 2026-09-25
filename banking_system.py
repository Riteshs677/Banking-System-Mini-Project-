"""
=====================================================
 BANKING SYSTEM - MINI PROJECT
=====================================================
A simple menu-driven Python application that simulates
basic banking operations such as account creation,
login, deposit, withdrawal, transfer, transaction
history, and PIN change.

Python Concepts Used:
- Variables & Data Types 782630, 810625
- Conditional Statements
- Loops
- Functions
- Lists & Dictionaries
- String Operations
- Modules (random, datetime)
=====================================================
"""

import random
from datetime import datetime

# ---------------------------------------------------
# In-memory "database" of accounts
# Structure:
# accounts = {
#     "100234": {
#         "name": "John Doe",
#         "phone": "9876543210",
#         "pin": "1234",
#         "balance": 5000.0,
#         "transactions": ["..."]
#     }
# }
# ---------------------------------------------------
accounts = {}



# Helper Functions

def generate_account_number():
    """Generate a unique 6-digit account number using random module."""
    while True:
        acc_no = str(random.randint(100000, 999999))
        if acc_no not in accounts:
            return acc_no


def get_timestamp():
    """Return current date & time as a formatted string using datetime module."""
    return datetime.now().strftime("%d-%m-%Y %I:%M %p")


def add_transaction(acc_no, description):
    """Add a record to the account's transaction history list."""
    entry = f"[{get_timestamp()}] {description}"
    accounts[acc_no]["transactions"].append(entry)


def press_enter_to_continue():
    input("\nPress Enter to continue...")


def print_header(title):
    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)


# Core Banking Features

def create_account():
    print_header("CREATE NEW ACCOUNT")
    name = input("Enter your full name: ").strip().title()

    while True:
        phone = input("Enter your phone number (10 digits): ").strip()
        if phone.isdigit() and len(phone) == 10:
            break
        print("Invalid phone number. Please enter exactly 10 digits.")

    while True:
        pin = input("Create a 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            break
        print("PIN must be exactly 4 digits.")

    acc_no = generate_account_number()
    accounts[acc_no] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }
    add_transaction(acc_no, "Account created")

    print("\nAccount created successfully!")
    print(f"Your Account Number is: {acc_no}")
    print("Please save this number safely - you will need it to log in.")
    press_enter_to_continue()


def login():
    print_header("LOGIN")
    acc_no = input("Enter Account Number: ").strip()

    if acc_no not in accounts:
        print("Account not found. Please check the account number.")
        press_enter_to_continue()
        return None

    pin = input("Enter PIN: ").strip()
    if accounts[acc_no]["pin"] != pin:
        print("Incorrect PIN.")
        press_enter_to_continue()
        return None

    print(f"\nWelcome back, {accounts[acc_no]['name']}!")
    press_enter_to_continue()
    return acc_no


def check_balance(acc_no):
    print_header("ACCOUNT BALANCE")
    print(f"Account Holder : {accounts[acc_no]['name']}")
    print(f"Account Number : {acc_no}")
    print(f"Current Balance: Rs. {accounts[acc_no]['balance']:.2f}")
    press_enter_to_continue()


def deposit(acc_no):
    print_header("DEPOSIT MONEY")
    try:
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            accounts[acc_no]["balance"] += amount
            add_transaction(acc_no, f"Deposited Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} deposited successfully!")
            print(f"New Balance: Rs. {accounts[acc_no]['balance']:.2f}")
    except ValueError:
        print("Invalid amount entered.")
    press_enter_to_continue()


def withdraw(acc_no):
    print_header("WITHDRAW MONEY")
    try:
        amount = float(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > accounts[acc_no]["balance"]:
            print("Insufficient balance.")
        else:
            accounts[acc_no]["balance"] -= amount
            add_transaction(acc_no, f"Withdrew Rs. {amount:.2f}")
            print(f"Rs. {amount:.2f} withdrawn successfully!")
            print(f"New Balance: Rs. {accounts[acc_no]['balance']:.2f}")
    except ValueError:
        print("Invalid amount entered.")
    press_enter_to_continue()


def transfer(acc_no):
    print_header("TRANSFER MONEY")
    receiver_acc = input("Enter receiver's account number: ").strip()

    if receiver_acc not in accounts:
        print("Receiver account does not exist.")
    elif receiver_acc == acc_no:
        print("You cannot transfer money to your own account.")
    else:
        try:
            amount = float(input("Enter amount to transfer: Rs. "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > accounts[acc_no]["balance"]:
                print("Insufficient balance.")
            else:
                accounts[acc_no]["balance"] -= amount
                accounts[receiver_acc]["balance"] += amount
                add_transaction(acc_no, f"Transferred Rs. {amount:.2f} to A/C {receiver_acc}")
                add_transaction(receiver_acc, f"Received Rs. {amount:.2f} from A/C {acc_no}")
                print(f"Rs. {amount:.2f} transferred successfully to account {receiver_acc}!")
                print(f"New Balance: Rs. {accounts[acc_no]['balance']:.2f}")
        except ValueError:
            print("Invalid amount entered.")
    press_enter_to_continue()


def view_transaction_history(acc_no):
    print_header("TRANSACTION HISTORY")
    history = accounts[acc_no]["transactions"]
    if not history:
        print("No transactions yet.")
    else:
        for i, record in enumerate(history, start=1):
            print(f"{i}. {record}")
    press_enter_to_continue()


def change_pin(acc_no):
    print_header("CHANGE PIN")
    old_pin = input("Enter old PIN: ").strip()

    if old_pin != accounts[acc_no]["pin"]:
        print("Incorrect old PIN.")
        press_enter_to_continue()
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    confirm_pin = input("Confirm new PIN: ").strip()

    if not (new_pin.isdigit() and len(new_pin) == 4):
        print("New PIN must be exactly 4 digits.")
    elif new_pin != confirm_pin:
        print("PINs do not match.")
    else:
        accounts[acc_no]["pin"] = new_pin
        add_transaction(acc_no, "PIN changed")
        print("PIN changed successfully!")
    press_enter_to_continue()


# Menus

def account_menu(acc_no):
    while True:
        print_header(f"ACCOUNT MENU - {accounts[acc_no]['name']}")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(acc_no)
        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            transfer(acc_no)
        elif choice == "5":
            view_transaction_history(acc_no)
        elif choice == "6":
            change_pin(acc_no)
        elif choice == "7":
            print("\nLogging out... Returning to main menu.")
            press_enter_to_continue()
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")
            press_enter_to_continue()


def main_menu():
    while True:
        print_header("WELCOME TO PYTHON BANK")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            acc_no = login()
            if acc_no:
                account_menu(acc_no)
        elif choice == "3":
            print("\nThank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 3.")
            press_enter_to_continue()


# Program Entry Point

if __name__ == "__main__":
    main_menu()
