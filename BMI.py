import sys

print ("BMI: BODY MASS INDEX V0.1 gamma beta whatevs")
userWeight = input("Enter Your Weight (in Pounds): ")
userHeight = input("Enter Your Height (in inches): ")

BMI = (703 * float(userWeight)) / (float(userHeight) * float(userHeight))
print ("Your body mass index(BMI) is:" + str(BMI) + "%")
