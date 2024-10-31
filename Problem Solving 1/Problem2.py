num = input("Enter a number, and I will check if it is an armstrong number: " )
# number of digits in num string = exponent
exp = len(num)
# Initialize the variable to store the "Armstrong number"
arm_output = 0

for digit in num:
    # Raise each digit to the power of the number of digits, storing additions in arm_output
    arm_output += pow(int(digit), exp)

# Check if the input number is equal to the obtained Armstrong number
if num == str(arm_output):
    print(f"{num} is an Armstrong number !!")
else:
    print(f"{num} is not an Armstrong number ")