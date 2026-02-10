# Problem 2: Employee Performance Bonus

def main():
    try:
        # 1. Capture User Input
        salary = float(input("Enter annual salary: $"))
        score = float(input("Enter performance score (0-100): "))

        # 2. Determine Bonus Percentage using Ladder Logic
        # We check from highest to lowest to ensure the correct bracket is caught
        if score >= 90:
            bonus_pct = 0.20
        elif score >= 80:
            bonus_pct = 0.10
        elif score >= 70:
            bonus_pct = 0.05
        else:
            bonus_pct = 0.00

        # 3. Calculations
        bonus_amount = salary * bonus_pct

        # 4. Final Output
        print("-" * 25)
        print(f"Performance Bonus: {int(bonus_pct * 100)}%")
        print(f"Bonus Amount: ${bonus_amount:,.2f}")

    except ValueError:
        print("Error: Please enter numeric values for salary and score.")

if __name__ == "__main__":
    main()