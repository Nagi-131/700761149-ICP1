score = float(input("Enter the score:"))

if score> 100:
  print("Invalid score")

elif score >= 90:
  grade = "A"

elif score >=80:
  grade = "B"

elif score >= 70:
  grade = "C"

elif score >= 60:
  grade = "D"

else:
  grade = "F"

print(f"Your grade: {grade}")
