# Problem 3: Loan Risk Classification

def main():
    try:
        # 1. Capture User Input
        credit_score = int(input("Enter credit score: "))
        annual_income = float(input("Enter annual income: $"))

        # 2. Compound Conditional Logic
        # Both conditions must be True for the block to execute
        if credit_score >= 720 and annual_income >= 60000:
            risk_category = "Low Risk"
            
        elif credit_score >= 650 and annual_income >= 40000:
            risk_category = "Medium Risk"
            
        else:
            risk_category = "High Risk"

        # 3. Final Output
        print("-" * 25)
        print(f"Loan Risk Category: {risk_category}")

    except ValueError:
        print("Invalid input. Please enter numbers for both score and income.")

if __name__ == "__main__":
    main()