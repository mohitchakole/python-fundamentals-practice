weight = float(input(f"enter your weight"))
unit = input("kilograms or pounds ? (k or p ):")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is : {round(weight, 2)} {unit}")

elif unit == "p":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is : {round(weight, 2)} {unit}")

else:
    print("unit was not valid ")
