for i in range(0,11):
    print(i)

number = int(input("Enter a number: "))
for x in range(1,11):
    print(f"{number} x {x} = {number * x}")

count = 0
total = 0
while count < 101:
    count += 1
    total += count

print(f"Total: {total}")

word = "programming"
for letter in word:
    print(letter)

nums = [12,7,45,3,28,9]
for num in nums:
    if num > 30:
        print(f"{num} is big number")

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")