N= int(input("Enter a number: "))

#initializing output list
output= []

#loop values from 1 to N
for n in range(1,int(N)+1):
    output.append(n)
    repeats= N-1 
    while repeats != 0: #appends further n values to output list N times
        output.append(n)
        repeats -= 1
print(output)