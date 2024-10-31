# Get user input for the number
num = int(input("Enter a positive number to find its square root: "))

# Determine the initial estimate with half the number of digits
a_n = 10 ** (len(str(num)) // 2)

e = 0.00001  # Set the small value for convergence

while True:
    a_n_minus_1 = a_n
    a_n = 0.5 * (a_n_minus_1 + num / a_n_minus_1)
    if abs(a_n - a_n_minus_1) < e: # Loop continues until this statement is True
        break

print(f"The square root of {num} is approximately {a_n}")
