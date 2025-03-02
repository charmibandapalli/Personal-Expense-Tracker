expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def show_expenses():
    for e in expenses:
        print(f"{e['category']}: ${e['amount']}")

if __name__ == "__main__":
    add_expense(50, "Food")
    add_expense(20, "Transport")
    show_expenses()
