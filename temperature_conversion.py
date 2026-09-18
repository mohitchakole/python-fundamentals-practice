unit = input("enter the unit of temperature (C or F):")
temp = float(input("enter the temperature:"))

if unit == "C":
    temp = round((temp*9)/5 + 32,1)
    print(f"the temperature in Fahrenheit is : {temp} F")

elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"the temperature in Celsius is : {temp} C")  

else:
    print("unit was not valid ")
        
    