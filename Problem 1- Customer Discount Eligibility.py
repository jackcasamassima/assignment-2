# Problem 1: Customer Discount Eligibility

def main():
    # 1. Capture User Input
    try:
        purchase_amt = float(input("Enter purchase amount: $"))
        is_member = input("Are you a member? (yes/no): ").strip().lower()

        discount = 0

        # 2. Apply Business Rules via Conditional Logic
        if is_member == "yes":
            if purchase_amt >= 100:
                discount = 0.15  # 15%
            else:
                discount = 0.05  # 5%
        else:
            if purchase_amt >= 150:
                discount = 0.10  # 10%
            else:
                discount = 0.00  # No discount

        # 3. Calculations
        savings = purchase_amt * discount
        final_price = purchase_amt - savings

        # 4. Final Output
        print("-" * 20)
        print(f"Discount applied: {int(discount * 100)}%")
        print(f"Final price: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the purchase amount.")

if __name__ == "__main__":
    main()