# A list of dictionaries where each dictionary represents one transaction
transactions = []


def add_transaction(transactions):
   # Ensures user enters a valid transaction type to keep data consistent
   while True:
       transaction_type = input("\nEnter transaction type (Income/Expense): ").lower().strip()  # .lower() keeps input case-insensitive and .strip() removes extra whitespace from user input
       if transaction_type in ["income", "expense"]:
           break
       else:
           print("\nInvalid input! Enter 'income' or 'expense'")


   # Ensures user enters a valid number to prevent calculation errors later
   while True:
       try:
           amount = float(input("\nEnter Amount: "))
           if amount <= 0:
               print("\nInvalid input! Amount must be positive")
           else:
               break
       except ValueError:
           print("\nInvalid input! Enter a number")


   if transaction_type == "income":
       categories = ["Salary", "Bonus", "Other"]
   else:
       categories = ["Rent", "Groceries", "Utilities"]


   # Displays category menu
   print("\nSelect transaction category: ")
   for i in range(len(categories)):
       print(f"{i + 1}. {categories[i]}")  # Creates numbered list of categories


   # Ensures category choice is within index range to avoid out of range errors
   while True:
       try:
           category_choice = int(input("\nEnter category number: "))
           # Check input within the valid menu range
           if 1 <= category_choice <= len(categories):
               break
           else:
               print("\nInvalid category number!")
       except ValueError:
           print("\nEnter a number")


   # Validate date input using format, type and range checks
   while True:
       # Checks there are exactly two hyphens for the correct format
       date = input("\nEnter date (DD-MM-YYYY): ")
       if date.count("-") != 2:
           print("\nInvalid format! Use DD-MM-YYYY format")
           continue


       split_date = date.split("-")


       # Checks split date contains day, month and year
       if len(split_date) != 3:
           print("\nInvalid format! Use DD-MM-YYYY format")
           continue


       day = split_date[0]
       month = split_date[1]
       year = split_date[2]


       try:
           day = int(day)
           month = int(month)
           year = int(year)


       except ValueError:
           print("\nInvalid date! Use numbers")
           continue


       # Validate ranges for each part of the date 
       if day < 1 or day > 31:
           print("\nInvalid day!")
           continue


       if month < 1 or month > 12:
           print("\nInvalid month!")
           continue


       if year < 1111 or year > 9999:
           print("\nInvalid year")
           continue
       break


   # Creates a structured record so each transaction keeps the related fields together
   transaction = {
       "type": transaction_type,
       "amount": amount,
       "category": categories[category_choice - 1],  # Converts user input (1-based) to Python index (0-based)
       "date": date
   }


   # Stores transaction in the main list so it can be accessed later
   transactions.append(transaction)
   print(f"\nTransaction added: {transaction['type'].capitalize()}, £{transaction['amount']:.2f}, {transaction['category']}, {transaction['date']}")


# Function to display all stored transactions
def view_transactions(transactions):
   if not transactions:   # Checks if transaction list is empty
       print("\nNo transactions")
       return  # Stops function


   print("\nAll transactions")
   # Use enumerate to display numbered transactions to match the menu
   for i, transaction in enumerate(transactions, start=1):
       print(f"{i}. {transaction['type'].capitalize()}, £{transaction['amount']:.2f}, {transaction['category']}, {transaction['date']}")


# Function to remove a user-selected transaction
def delete_transactions(transactions):
   if not transactions:  # Checks if transaction list is empty
       print("\nNo transactions")
       return


   print("\nAll transactions")
   # Use enumerate to display numbered transactions to match the menu
   for i, transaction in enumerate(transactions, start=1):
       print(f"{i}. {transaction['type'].capitalize()}, £{transaction['amount']:.2f}, {transaction['category']}, {transaction['date']}")


   # Validate input to ensure user selects a valid transaction index
   while True:
       try:
           user_choice = input("\nSelect transaction number to delete: ")
           index = int(user_choice) - 1   # Converts user input (1-based) to Python index (0-based)
           if 0 <= index < len(transactions):
               break
           else:
               print("\nInvalid transaction number!")


       except ValueError:
           print("\nEnter a number")


   # Removes selected transaction from list and returns it for confirmation
   deleted_transaction = transactions.pop(index)
   print(f"\nDeleted transaction: {deleted_transaction['type'].capitalize()}, £{deleted_transaction['amount']:.2f}, {deleted_transaction['category']}, {deleted_transaction['date']}")


# Function to display transactions that match the category entered by the user
def filter_transactions(transactions):
   if not transactions:  # Checks if transaction list is empty
       print("\nNo transactions")
       return  # Stops function


   target_category = input("\nFilter by which category (e.g. rent, groceries)? ").lower().strip()
   found = False  # For if no matching transactions


   # Checks each transaction and only displays transactions matching the user's chosen category
   for transaction in transactions:
       # Case-insensitive comparison for if user types different capitalisation, allows for filtering later
       if transaction["category"].lower() == target_category:
           if not found:
               print("\nFiltered transactions")
           print(f"{transaction['type'].capitalize()}, £{transaction['amount']:.2f}, {transaction['category']}, {transaction['date']}")
           found = True
   if not found:
       print("\nNo transactions found for this category")


# Function to calculate the total income by adding amounts from income transactions only
def calculate_total_income(transactions):
   total = 0
   # Iterate through all transactions and check if the transaction is an income
   for transaction in transactions:
       if transaction["type"] == "income":
           total += transaction["amount"]
   return total


# Function to calculate the total expense by adding amounts from expense transactions only
def calculate_total_expense(transactions):
   total = 0
   # Iterate through all transactions and check if the transaction is an expense
   for transaction in transactions:
       if transaction["type"] == "expense":
           total += transaction["amount"]
   return total


# Calculates the remaining balance by subtracting total expenses from total income
def calculate_remaining_balance(transactions):
   total_income = calculate_total_income(transactions)
   total_expense = calculate_total_expense(transactions)
   remaining_balance = total_income - total_expense


   return remaining_balance


# Groups and totals expenses by category using a dictionary to keep amounts together
def get_expense_category_totals(transactions):
   expense_totals = {}   # Dictionary to store total expense amount for each category


   # Build category totals by iterating through expense transactions
   for transaction in transactions:
       if transaction["type"] == "expense":
           category = transaction["category"]
           amount = transaction["amount"]


           # If category not in dictionary yet, this creates one with an initial amount
           if category not in expense_totals:
               expense_totals[category] = amount
           else:
               expense_totals[category] = expense_totals[category] + amount
   return expense_totals


def get_highest_expense_category(transactions):
   # To get total expenses grouped by category
   expense_totals = get_expense_category_totals(transactions)
   # For if no expense data exists
   if not expense_totals:
       return None


   highest_expense_category = None
   highest_total = None


   # Compares category totals to find the highest value
   for category in expense_totals:
       current_total = expense_totals[category]


       if highest_expense_category is None or current_total > highest_total:
           # Initial None value allows the first category total to become the starting comparison point
           highest_expense_category = category
           highest_total = current_total


   return highest_expense_category, highest_total


def get_lowest_expense_category(transactions):
   # To get total expenses grouped by category
   expense_totals = get_expense_category_totals(transactions)
   # For if no expense data exists
   if not expense_totals:
       return None


   lowest_expense_category = None
   lowest_total = None


   # Compares category totals to find the lowest value
   for category in expense_totals:
       current_total = expense_totals[category]


       if lowest_expense_category is None or current_total < lowest_total:
           # Initial None value allows the first category total to become the starting comparison point
           lowest_expense_category = category
           lowest_total = current_total


   return lowest_expense_category, lowest_total


# Function to display a summary of transaction data by combining results from multiple calculation functions
def show_summary(transactions):
   if not transactions:
       print("\nNo transactions!")
       return


   total_income = calculate_total_income(transactions)
   total_expense = calculate_total_expense(transactions)
   remaining_balance = calculate_remaining_balance(transactions)


   highest = get_highest_expense_category(transactions)
   lowest = get_lowest_expense_category(transactions)


   print("\nSummary: ")
   print(f"Total income: £{total_income:.2f}")
   print(f"Total expense: £{total_expense:.2f}")
   print(f"Remaining balance: £{remaining_balance:.2f}")


   if highest is not None:
       highest_category, highest_total = highest
       print(f"Highest expense: {highest_category}, £{highest_total:.2f}")
   else:
       print(f"No expenses for highest category")


   if lowest is not None:
       lowest_category, lowest_total = lowest
       print(f"Lowest expense: {lowest_category}, £{lowest_total:.2f}")
   else:
       print(f"No expenses for lowest category")


# Shows user menu options
while True:
   print("\nFinancial Tracker Menu")
   print("1. Add transaction")
   print("2. View all transactions")
   print("3. Delete transaction")
   print("4. Filter by category")
   print("5. Show summary")
   print("6. Exit")    


   # Ensures user selects a valid menu option to prevent unexpected behaviour
   while True:
       choice = input("\nEnter option: ")
       if choice in ["1", "2", "3", "4", "5", "6"]:
           break
       else:
           print("\nInvalid menu option!")


   if choice == "1":
       add_transaction(transactions)
   elif choice == "2":
       view_transactions(transactions)
   elif choice == "3":
       delete_transactions(transactions)
   elif choice == "4":
       filter_transactions(transactions)
   elif choice == "5":
       show_summary(transactions)
   elif choice == "6":
       break