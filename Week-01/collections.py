nums = [45, 12, 78, 3, 90, 23]

nums.sort()
print(nums)

biggest = nums[0]
for num in nums:
    if num > biggest:
        biggest = num
print(f"The biggest number is {biggest}")

total = 0
for num in nums:
    total = total + num
print(f"The total of the numbers is {total}")

average = total / len(nums)
print(f"The average of the numbers is {average}")

num = []

num.append(int(input("Enter a number 1: ")))
num.append(int(input("Enter a number 2: ")))
num.append(int(input("Enter a number 3: ")))
num.append(int(input("Enter a number 4: ")))
num.append(int(input("Enter a number 5: ")))

print(num)

words = ["apple", "banana", "kiwi", "fig", "cherry"]
letter_words = []

for word in words:
    if len(word) > 5:
        letter_words.append(word)

print(letter_words)

my_dict = {"name": "Akshayan", "age": 22, "city": "srilanka", "hobby 1": "reading", "hobby 2": "coding"}

my_dict.values()

print(my_dict.values())

marks = {"maths": 85, "science": 72, "english": 91}
mark = marks.values()

print(mark)

total_marks = 0
for average in mark:
    total_marks += average
average_marks = total_marks / len(marks)
print(average_marks)

