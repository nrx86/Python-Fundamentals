# #Even or odd number#
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

marks=[67, 45, 89, 90, 56, 78]
total=0
for mark in marks:
    total += mark

average = total / len(marks)
print("The average marks is:", average)