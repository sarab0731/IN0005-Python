# number of guesses available
N = 3
print(f"Welcome to Pointless! A game where the lowest scorers are the biggest winners! You will have {N} guesses to get the correct answer.")

# declaring answer variables and their respective points
answers = ["norway", "newzealand", "netherlands", "nigeria", "north korea", "niger", "nicaragua", "namibia", "nepal", "nauru"]
points = [48, 45, 41, 29, 13, 11, 9, 2, 1, 0]

while N >= 1: # exits loop when number of guesses are less than 1
    user_answer = input("Name a country beginning with N: ")
    i = 0

    for answer in answers:
        if user_answer.lower() == answer:
            score = points[i]
            print(f"Correct answer, +{score} points!")
            if score == 0:
                print("Well done!! You have guessed a pointless answer")
            break # exits loop if the answer is correct
        else:
            i = i + 1
            continue # moves to the next iteration of the loop

    if user_answer.lower() == answer:
        break # exits while loop if the answer is correct

    N = N - 1 # for each incorrect answer, num of guesses are reduced by one
    
    # messages for incorrect outcomes
    if N == 1:
        print(f"Incorrect! You have {N} guess left")
    else:
        print(f"Incorrect! You have {N} guesses left")
    if N == 0: # when there are no guesses left
        print("Better luck next time!")
        
