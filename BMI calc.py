def gather_info():
    height = float(input("What is your height?(inch or meter)"))
    weight = float(input("What is your weight?(pounds or kg)"))
    system = input("Are your measurements in metric or imperial units?").lower().strip()  # .strip() is to remove spaces bef and aft the answer like "  metric   " to "metric"
    return height, weight, system


def calculate_bmi(weight, height, system="metric"):  # Return the BMI for the given height weight measurement
    if system == "metric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi


while True:
    height, weight, system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error")
