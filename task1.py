
s = input("Enter a string: ")
if len(s) >= 2:
    sub_string=s[:-2]
    result_str = sub_string[::-1]
    print("Processed string:", result_str)
else:
    print("String too short")


a= float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum=a+b
diff = a-b
mul = a*b

if b!=0:
  div = a/b
else:
  div="undefined"

print(f"Sum: {sum}, Difference: {diff}, Product: {mul}, Division: {div}")
