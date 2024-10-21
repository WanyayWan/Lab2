def calculate_bmi(height, weight):
    print("Height = " + str(height) + " cm")
    print("Weight = " + str(weight) + " kg")
    
    # Convert height from cm to meters
    height_in_meters = height / 100

    # Calculate BMI
    bmi = weight / (height_in_meters ** 2)

    # Display the calculated BMI
    print("Your BMI is = " + str(round(bmi, 2)))

    # Check BMI category
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")

# Call the function with sample data
calculate_bmi(weight=57, height=173)