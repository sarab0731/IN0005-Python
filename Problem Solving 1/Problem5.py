N = int(input("Enter the amount of numbers in the Stern-Brocot sequence you want to generate: "))

# Starting point of the sequence
stern_brocot = [1,1]

# Variable to keep track of the index in the sequence
i= 0

# Generating the sequence until it has N numbers
while len(stern_brocot) < N:
    a = stern_brocot[i]
    b = stern_brocot[i + 1]
    c = a + b # Calculate the sum of the current and next number
    stern_brocot.append(c)
    stern_brocot.append(b)
    i +=1

# Trimming the sequence to have only the desired amount of numbers
stern_brocot= stern_brocot[:N]

# Copying the sequence for further processing
sb_copy = stern_brocot.copy()

# Removing the last number if the sequence length is odd
if len(sb_copy)%2 != 0:
    sb_copy.pop(-1)

r_list = []
i= 0

# Converting the numbers into fractions
while i < N-1:
    a= sb_copy[i]
    b= sb_copy[i + 1]
    c= f"{a}/{b}" # Create a string representation of the fraction
    r_list.append(c) # Add the fraction to the list
    i +=1

if len(stern_brocot) == 1:
    print(f"The sequence is: {stern_brocot}")
    print("There are no rational numbers for this sequence.")
else:
    print(f"The sequence is: {stern_brocot}")
    print(f"The rational numbers are: {r_list}")