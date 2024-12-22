def display_summary(expenses):
    total_expenses = sum(expenses.values())
    if total_expenses == 0:
        print("\nNo expenses recorded yet.")
        return
    
    print("\nExpense Summary:")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    for category, amount in expenses.items():
        percentage = (amount / total_expenses) * 100
        print(f" - {category}: ₹{amount:.2f} ({percentage:.2f}%)")

def main():
    categories = ["Food", "Transport", "Entertainment", "Others"]
    expenses = {category: 0.0 for category in categories}

    print("Dynamic Expense Tracker")
    print("Categories: Food, Transport, Entertainment, Others\n")
    
    while True:
        print("\nOptions:")
        print("1. Add an Expense")
        print("2. Show Summary")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            print("\nCategories:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            category_choice = int(input("Select a category number: "))
            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]
                amount = float(input(f"Enter the expense amount for {category}: ₹"))
                expenses[category] += amount
                print(f"Added ₹{amount:.2f} to {category}.")
            else:
                print("Invalid category choice. Please try again.")
        
        elif choice == "2":
            display_summary(expenses)
        
        elif choice == "3":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
