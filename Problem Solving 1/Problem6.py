# Ask the user to input the coefficients of the quintic equation
print("input the coefficients of your quintic equation: ")
a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))
d= int(input("d= "))
e= int(input("e= "))
f= int(input("f= "))

# Ask the user to input an interval
print("input an interval [l,h] where f(l) and f(h) yield opposing signs: ")
l= int(input("l= "))
h= int(input("h= "))

soln= False
NMAX = 5000
TOL = 0.000001

# Loop through a certain number of iterations, specified by NMAX
for N in range(1, NMAX, 1):
    # Calculate the midpoint of the interval
    x= (l+h)/2

    # Calculate the value of the equation at the midpoint
    fx= a*(pow(x,5)) + b*(pow(x,4)) + c*(pow(x,3)) + d*(pow(x,2)) + e*x + f

    # Calculate the value of the equation at the lower end of the interval
    fl= a*(pow(l,5)) + b*(pow(l,4)) + c*(pow(l,3)) + d*(pow(l,2)) + e*l + f

    # Check if the value of the equation is zero or if the interval is very small
    if fx == 0 or (h-l)/2 < TOL:
        soln = True
        break

    # Check if the value of the equation at the midpoint and lower end have the same sign
    if fx*fl > 0:
        # If they have the same sign, update the lower end of the interval to the midpoint
        l= x
    else:
        # Otherwise, update the upper end of the interval to the midpoint
        h= x

if soln:
    # If a solution is found, print the value of the solution
    print(f"x= {x}")
else:
    print("Method failed.")
    