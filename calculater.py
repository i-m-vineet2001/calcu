#caluclater
first = input("Enter you 1st number :")
operator = input("Enter your operator[+,-,/,%.*] :")
second = input("Enter you second number :")
first=int(first)
second=int(second)
if operator == "+":
    print(first+second)
if operator == "*":
    print(first*second)
if operator == "-":
    print(first-second)
if operator == "%":
    print(first%second)
if operator == "/":
    print(first/second)
else:
    print("invalid number")


