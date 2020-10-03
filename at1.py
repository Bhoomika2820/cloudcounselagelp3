"""CODING QUESTIONS: 1
Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.
"""
a = int(input("Enter 1st no :"))
b = int(input("Enter 1st no :"))

print("sum :", a + b)
if a > b:
    print("diff :", a - b)
else:
    print("diff :", b - a)

print("product :", a * b)
