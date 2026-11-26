from random import random

for i in range(0,11):
    print(i)

number = int(input("Enter a number: "))
for x in range(1,11):
    print(f"{number} x {x} = {number * x}")

count = 0
total = 0
while count < 100:
    count = count + 1
    total = total + count
    print(f"Total: {total}")

word = "programming"
for letter in word:
    print(letter)

nums = [-12,-7,-45,-3,-28,-9]
biggest = float("-inf")
for num in nums:
    if num > biggest:
        biggest = num
print(f"The biggest number is {biggest}")

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"Factorial of {num} is {factorial}")

user_input = input("Enter a string: ")
while True:
    if user_input == "quit":
        break
    else:
        print(f"You entered: {user_input}")
        user_input = input("Enter a string (type 'quit' to quit): ")

for i in range(1,20):
    if i % 3 == 0:
        continue
    else:
        print(i)
