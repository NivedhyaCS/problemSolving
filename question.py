x=int(input("enter the body weight in kg:"))
y=float(input("enter the body height in m:"))
def BMI(x,y):
    BMI=x/(y*y)
    return BMI
BMI_CAL=(BMI(x,y))
print("enter BMI:",(BMI_CAL))
