from datetime import datetime

expenses = []

def add_expense(amount, category, date):
    """Add an expense to the in-memory list with rounded amount."""
    try :
        amount = round(amount, 2)
    except ValueError:
        print("Invalid amount. plz enter a nimeric value .")
        return
    
    try :
        datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        print ("plz use YYYY-MM-DD format.")
        return
    
    expenses.append({'amount': amount, 'category': category, 'date': date})
    print(f"Added expense: ${amount} in {category} on {date}")

def summarize_expenses():
    total = 0
    category_totals = {}
    for expense in expenses:
        amount = expense['amount']
        category = expense['category']
    
        total += amount
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    # print total expenses
    print(f"Total Expenses: ${round(total, 2)}")
    # print all seperate amount by category
    for category, amount in category_totals.items():
        print(f"Total in {category}: ${round(amount, 2)}")


def expense_trends():
    """Show all expenses by months."""
    trends = {}
    
    for expense in expenses:
        month = datetime.strptime(expense['date'], "%Y-%m-%d").strftime("%Y-%m")
        if month in trends:
            trends[month] += expense['amount']
        else:
            trends[month] = expense['amount']
    
    for month, amount in trends.items():
        print(f"Total for {month}: ${round(amount, 2)}")

def main():
    """Main function to run the expence tracker."""
    to_run = True
    while to_run:
        print("\nExpense Tracker")
        print("Add Expense")
        print("Show Summary")
        print("Show Expense Trends")
        print("Exit")
        choice = input("Choose an option: ").lower()

        if choice == 'add expense':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
        elif choice == 'show summary':
            summarize_expenses()
        elif choice == 'show expense trends':
            expense_trends()
        elif choice == 'exit':
            break
        else:
            print("Please choose a correct word from above. try again!")

main()