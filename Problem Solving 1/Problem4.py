x= int(input("x= "))
y= int(input("y= "))

hcf_list=[] # Creating an empty list to store the remainders
hcf= 0

# makes sure that x always has the largest value, and x, y are not equal.
if y > x:
    x, y = y, x
elif y == x:
    print("Error: the integers must not be equal")

a= x % y
b= x - a
hcf_list.append(a) # Adding the first remainder to the list of remainders

if a== 0:
    hcf= y

# Loop to calculate the HCF
while a!= 0:
    a= b % a
    b= b - a
    hcf_list.append(a)

hcf= hcf_list[-2] # The second last item in the list is the HCF
lcm = int(abs(x*y)/hcf) # Calculating the LCM 

print(f"HCF= {hcf}")
print(f"LCM= {lcm}")
