'''
A Python program to solve the
Quadratic function (ax2 + bx + c = 0) using
formula 
'''

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the valueof c"))

x1 = (-b + ((b*b) - (4 * a * c)) ** 0.5 )/2 * a
x2 = (-b - ((b*b) - (4 * a * c)) ** 0.5 )/2 * a

print("x1 = ", x1)
print("x2 = ", x2)

