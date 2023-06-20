#!/usr/bin/env python
# coding: utf-8

# # BMI Caluculator

# In[25]:


print("BMI Calculator")
Units = int(input("Select Units, 'Enter 1 for Kg,cm' / '2 for Pound/Inches'"))

if Units == 2:
    Weight = int(input("Enter Your Weight in Pounds: "))

    Height = int(input("Enter Your Height in Inches: "))

    BMI = (Weight*703) / (Height * Height)
    Rounded_BMI = round(BMI,2)
elif Units == 1:
    Weight = int(input("Enter Your Weight in Kilograms: "))

    Height = int(input("Enter Your Height in Centimeters: "))

    BMI = (Weight) *100**2 / (Height * Height)
    Rounded_BMI = round(BMI,2)
else:
    print("Please Enter a Valid Response")

print( "\nYour BMI is :" + str(Rounded_BMI)) 

if Rounded_BMI>0:
    if(Rounded_BMI<18.5):
        print("You Are Underweight")
    elif(Rounded_BMI<=24.9):
        print("You Are Normal Weight")
    elif(Rounded_BMI<=29.9):
        print("You Are Overweight")   
    elif(Rounded_BMI>=34.9):
        print("You Are Obese")       
    else: 
        print("Enter Valid Inputs")

