def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the Budget Tracker!")
    income = get_float_input("Enter your total income: $")
    expenses = get_float_input("Enter your total expenses: $")
    remaining_budget = income - expenses
    print(f"\nYour remaining budget is: ${remaining_budget:.2f}")
    save_to_csv = input("\nDo you want to save this data to a CSV file? (yes/no): ").strip().lower()
    if save_to_csv == "yes":
        import csv
        with open('budget_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Income", "Expenses", "Remaining Budget"])
            writer.writerow([income, expenses, remaining_budget])
        print("Data saved to 'budget_data.csv'.")

if __name__ == "__main__":
    main()