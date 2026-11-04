weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")

weight_lb = weight * 2.28462
print(f"Weight in pounds: {weight_lb:.1f}")