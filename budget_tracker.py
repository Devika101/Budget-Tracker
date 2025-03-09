import csv

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_csv_data():
    try:
        with open('budget_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No data found. Please save some data first.")

def main():
    print("Welcome to the Budget Tracker!")
    print("1. Add new budget entry")
    print("2. View existing data")
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == "1":
        income = get_float_input("Enter your total income: ")
        expenses = get_float_input("Enter your total expenses: ")
        remaining_budget = income - expenses
        print(f"\nYour remaining budget is: {remaining_budget:.2f}")
        save_to_csv = input("\nDo you want to save this data to a CSV file? (yes/no): ").strip().lower()
        if save_to_csv == "yes":
            with open('budget_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(["Income", "Expenses", "Remaining Budget"])
                writer.writerow([income, expenses, remaining_budget])
            print("Data saved to 'budget_data.csv'.")
    elif choice == "2":
        view_csv_data()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()