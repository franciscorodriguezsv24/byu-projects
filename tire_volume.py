##Hello this is my aplication to calculate the volume of a tire
import math
print("Welcome to the Tire Volume Calculator")
print("Please enter the following measurements in inches.")

w = float(input("Enter the width of the tire in mm (ex 205):"))
a = float(input("Enter the aspect ratio of the tire (ex 60):"))
d = float(input("Enter the diameter of the wheel in inches (ex 15):"))

volume = math.pi * w**2 * a * (w * a + 2540 * d) / 10000000000

volume = round(volume, 2)

print("The approximate volume is: " + str(volume) + " liters")