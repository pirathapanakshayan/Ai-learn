name = "Akshayan"
age = 22
height = 5.8
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

num_text = "42"
print(num_text + "8")
print(int(num_text) + 8)

user_number = input("Enter a number: ")
#print (user_number + 10)  # This will cause an error because user_number is a string
print (int(user_number) + 10)

a = 25
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

x = 10
y = "10"

print(x == 10)  # This will cause an error because X is not defined
print(x == y)
print(x == int(y))  # This will cause an error because X is not defined

print(True and False)
print(True or False)
print(not True)