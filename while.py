# #Even or odd number#
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# marks=[67, 45, 89, 90, 56, 78]
# total=0
# for mark in marks:
#     total += mark

# average = total / len(marks)
# print("The average marks is:", average)

#Write a program to print sum of digits
# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print("Sum of digits is:",sum)

#Write a program to print reverse of a number
n=int(input("Enter a number:"))
r=0
while n>0:
    r=r*10+n%10
    n=n//10
print("Reverse of the number is:", r)
