def classify_number(n):
    n=int(input("Input:"))
if n>0 and n%2==0:
    print("Positive Even")
elif n>0 and n%2!=0:
    print("Positive Odd")
elif n<0 and n%2==0:
    print("Negative Even")
elif n<0 and n%2!=0:
    print ("Negative Odd")
if n==0:
    print("Zero")