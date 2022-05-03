def Bmi_Calc():
    unit = input("will you use imperial or metric?: ")

    if unit == "metric":
        h_metres = float(input("please give me your height in metres: "))
        w_kilograms = float(input("enter your weight in kilograms: "))
        bmi_met = w_kilograms / h_metres**2
        print(f"your bmi is {bmi_met:.2f} kg/m2")
        if bmi_met >= 18 or bmi_met <= 25:
            print("you are a in good shape")
        elif bmi_met < 18:
            print("you are malnourished of sorts")
        elif bmi_met > 25:
            print("you are overweight")

    elif unit == "imperial":
        h_inches = float(input("please give me your height in inches: "))
        w_pounds = float(input("enter your weight in pounds: "))
        bmi_imp = (w_pounds / h_inches**2) * 703
        print(f" your bmi is {bmi_imp:.2f} kg/m2")
        
        if bmi_imp >= 18 and bmi_imp <= 25:
            print("you are in good shape")
        elif bmi_imp < 18:
            print("your are malnourished of sorts")
        elif bmi_imp > 25:
            print("you are overweight")

    else:
        print("please enter the correct unit of measurement")
        Bmi_Calc()

Bmi_Calc()
