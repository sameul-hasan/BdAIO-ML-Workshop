# Write a python function to print multiplication table of a given number.
def table(n):
    for i in range(1,n+1):
        print(f"{n}X{i}={n*i}")
n = int(input("Enter the number: "))
table(n)