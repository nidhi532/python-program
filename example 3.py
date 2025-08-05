# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to determine health category based on BMI
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to handle one person's BMI check
def bmi_check():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"\n{name}, your BMI is: {bmi}")
    print(f"Health Category: {category}")

# Main function to run the program
def main():
    print("=== BMI Calculator ===")
    while True:
        bmi_check()

        choice = input("\nDo you want to check another person? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the BMI calculator!")
            break

main()

