def bmi_calculator(height,weight):
    global bmi
    if height<=0.0 or weight<=0.0:
        print("Sorry mate,you've entered invalid details,enter valid ones.")
    elif height>270 or weight>300:
        print("Inputs are quite out of range,check and re-enter them. ")
    else:
        bmi = round(weight / height ** 2,2)
        print("Calculated BMI is: ",bmi)
        categorization(bmi)
def categorization(bmi):
    if bmi < 18.5:
        print("Underweight,u gotta gain some weight buddy!")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Normal,no worries,you're perfect dude!.")
    elif bmi >= 25.0 and bmi <= 29.9:
        print("Overweight,try taking a good diet.")
    elif bmi >= 30.0 and bmi <= 34.9:
        print("Obesity(class I),take a good diet.")
    elif bmi >= 35.0 and bmi <= 39.9:
        print("Extreme obesity,take a good diet.")
    else:
        print("Obesity(class,take a good diet.")
print("Hey user,let me help you in calculating your Body Mass Index!")
height=float(input("Enter your height(in meters):"))
weight=float(input("Enter your weight(in kilograms):"))
bmi_calculator(height,weight)
