hidden_list_a = [0,0,0,0,0,0,0,0]
hidden_list_b = [0,0,0,0,0,0,0,0]

# setting the values for list a and b which the user will slowly reveal
list_a = [6,8,2,1,9,3,5,7]
list_b = [5,3,1,9,7,6,8,2]

print(hidden_list_a)
print(hidden_list_b)


while hidden_list_a.count(0) > 0 and hidden_list_b.count(0) > 0:
    choice1 = int(input("Which position do you want to check in the first row?: ")) - 1
    chosen_num1 = list_a[choice1]
    
    a= hidden_list_a.copy()
    a.pop(choice1)
    a.insert(choice1, chosen_num1)
    
    
    print(a)
    print(hidden_list_b)
    
    choice2 = int(input("Now guess where that number is in the second row: ")) -1 
    
    chosen_num2 = list_b[choice2]
    b= hidden_list_b.copy()
    b.pop(choice2)
    b.insert(choice2, chosen_num2)
    print(a)
    print(b)    

    if chosen_num1 == chosen_num2:

        hidden_list_a = a
        hidden_list_b = b
    else:
        print("Try again!")
        print(hidden_list_a)
        print(hidden_list_b)
        continue

print("Congratulations! You have completed the game ")
