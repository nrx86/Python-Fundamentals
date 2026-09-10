# #numbers 1-10 using for loop
# for i in range(1, 11):
#     print(i)

# #how to find which number is on which index
l1=[45, 67, 89, 90, 56, 78]
target=90
for i in range(len(l1)):
    if l1[i] == target:
        print("Found at index:", i)
        break
else:
    print("Target not found.")