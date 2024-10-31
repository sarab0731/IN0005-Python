n = int(input("Enter a number n: "))  # Takes user input for n

# initialize variable for superfactorial
sf = 1

while n > 0:  # Loop until n becomes zero
    n_f = 1  # Initialize n_f for factorial calculation
    for N in range(1, n + 1):  # Computes factorial of n
        n_f *= N
    sf *= n_f  # Multiply superfactorial by calculated factorial
    n -= 1  # Decrement n in each iteration

print(sf)
