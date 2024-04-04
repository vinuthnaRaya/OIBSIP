def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (in kilograms) and height (in meters).
    Formula: BMI = weight / (height ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify BMI into categories based on predefined ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()
