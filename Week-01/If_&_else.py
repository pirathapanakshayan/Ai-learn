print("Task one: Check if a number is positive, negative, or zero")
print("==========================================================")
print(                                                            )

number = int(input("Enter the number: "))

if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")

print("Task two: Check if a number is even or odd")
print("==========================================")
print(                                            )

numbe = int(input("Enter the number: "))

if numbe % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

print("Task three: Check the grade based on marks")
print("==========================================")
print(                                            )

marks = int(input("Enter the marks: "))

if marks >= 75:
    print("Grade: A")
elif marks >= 65:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: S")
else:
    print("Grade: F")

print("Task four: Check which number is greater")
print("========================================")
print(                                          )

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

print("Task five: Check your age group")
print("================================")
print(                                        )

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

print("Task six: Check login credentials")
print("=================================")
print(                                   )

user_name = input("Enter your user name: ")
password = input("Enter your password: ")

if user_name == "admin" and password == "admin123":
    print("Login successful!")
    print("Welcome,", user_name)
else:
    print("Invalid username or password.")