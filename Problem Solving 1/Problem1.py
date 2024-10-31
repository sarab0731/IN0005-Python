user_name = input("Please enter your full name: ")
birth_year = int(input("To find your generation, please enter your birth year: "))
generation = ""

# determines an invalid birth year
if birth_year < 1901 or birth_year > 2023:
    print("Error: there are no recorded people in your birth year")
# determines the generation
else:
    if 1901 <= birth_year <= 1924:
        generation = "from the Greatest Generation"
    elif 1925 <= birth_year <= 1945:
        generation = "from the Silent Generation"
    elif 1946 <= birth_year <= 1964:
        generation = "a Baby Boomer"
    elif 1965 <= birth_year <= 1980:
        generation = "from Generation X"
    elif 1981 <= birth_year <= 1996:
        generation = "a millenial"
    elif 1997 <= birth_year <= 2012:
        generation = "from Generation Z"
    else:
        generation = "from Generation Alpha"

# prints the output message
print(f"Hello {user_name.title()}, you are {generation}")