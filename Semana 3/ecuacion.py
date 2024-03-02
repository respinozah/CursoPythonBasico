import os
os.system("cls")
#x = 0
a = 2
b = 4
c = -6

discriminant = (b**2) - (4*a*c)
x = (-b + discriminant**0.5) / (2*a)
print("The value of X, using add is: ", x)

x = (-b - discriminant**0.5) / (2*a)
print("The value of X, using substraction is: ", x)
