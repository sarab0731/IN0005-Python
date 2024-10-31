def register():
    """
    The purpose of this function is to register a new user with the provided username
    If the username already exists, it would then prompt the user to choose another username
    It would then save the user's username in a usernames.txt file .
    prints "User registered successfully" when a  unique username is entered
    
    Parameters
    ----------
    no parameters- username(str) variable would be defined within function
    
    Returns 
    -------
    username
    """
    username = input("Enter your preferred username: ").title()
    while username_found(username):
        print("Invalid username. This username already exists")
        username = input("Please enter a unique username: ").title()
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")
    print("...")
    print("Registered successfully.")
    return username

def login():
    """
    This function identifies whether the username provided by the user already exists.
    If it exists, then it validates the username and continues the code, 
    else it prompts the user to enter a valid username until one is provided.
    
    Parameters
    ----------
    no parameters- username(str) variable would be defined within function
    
    Returns 
    -------
    username
    """
    username = input("Please enter your registered username: ").title()
    while True:
        if username_found(username):
            print("...")
            print("Login successful.")
            return username
        else:
            username = input("Please enter a valid username: ").title()

def username_found(username):
    """
    This function is used inside both the register and login functions. 
    It opens the usernames.txt file in read mode and searches for the username
    
    Parameters
    ----------
    username : str 
    
    Returns 
    -------
    bool
        True if username is found in usernames.txt, False otherwise.
    """
    try:
        with open("usernames.txt", "r") as file:
            usernames = [line.strip() for line in file]
        if username in usernames:
            return True
        else:
            return False
                    
    except IOError:
        with open("usernames.txt", "w") as file:
            # file is empty so username not found. return false
            return False

def menu(username):
    """
    This is the user menu function. It deals with handling the user's choices within the theatre ticketing system
    displays 4 options: 
        1. Book ticket
        2. Cancel ticket(s)
        3. Show ticket(s)
        4. Exit                
    checks for user errors- i.e. when a user enters a number that is not 1-4
        
    Parameters
    ----------
    username : str
        represents the username of the normal user currently logged in.
        Used when calling other functions, such as book_ticket(username), cancel_ticket(username), and show_tickets(username).
        These functions require the username information to access and manipulate user-specific data, 
        such as booking history and ticket information.
        
    """
    online = True
    while online:
        print()
        print("Menu:")
        print("1. Book ticket")
        print("2. Cancel Ticket(s)")
        print("3. Show ticket(s)")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        print()
    
        if choice == 1:
            print("Book ticket:\n")
            
            display_theatre(username, 'b')
            book_ticket(username)
            
            while True:
                back_to_menu = int(input("To return to menu, enter 1. To quit, enter 0: "))
                if back_to_menu == 0:
                    online = False
                    print("Exiting ticketing system...")
                    break 
                elif back_to_menu == 1:
                    break
                else:
                    print("Invalid input, please try again.")
                    
        elif choice == 2:
            print("Cancel Ticket:\n")
            display_theatre(username, 'c')
            cancel_ticket(username)
            
            while True:
                back_to_menu = int(input("To return to menu, enter 1. To quit, enter 0: "))
                if back_to_menu == 0:
                    online = False
                    print("Exiting ticketing system...")
                    break 
                elif back_to_menu == 1:
                    break
                else:
                    print("Invalid input, please try again.")
        elif choice == 3:
            print("Show Ticket(s):\n")
            user_tickets = load_user_info(username)
            show_ticket(user_tickets)
            
            while True:
                back_to_menu = int(input("To return to menu, enter 1. To quit, enter 0: "))
                if back_to_menu == 0:
                    online = False
                    print("Exiting ticketing system...")
                    break 
                elif back_to_menu == 1:
                    break
                else:
                    print("Invalid input, please try again.")
        elif choice == 4:
            print("Exiting ticketing system...")
            break
        else:
            print("Invalid choice, please try again.")
    
def load_user_info(username):
    """
    This function loads the user information from the text file.
    It reads each line of the file and filters out the lines corresponding to the specified username.
    The function constructs a list of dictionaries from the saved info in the text file, where each dictionary represents one of the user's booked tickets.
    Each dictionary contains the ticket information, including the row number, seat number, and price.
    
    Parameters
    ----------
    username : str
        Represents the username of the normal user currently logged in.
        Used to filter the user's booking history from the text file.
    
    Returns
    -------
    list
        A list of dictionaries, where each dictionary represents one of the user's booked tickets.
        Each dictionary contains the ticket information, including the row number, seat number, and price.
    """
    user_tickets = []
    try:
        with open("ticket_database.txt", "r") as file:
            count = 0
            for line in file:
                ticket_info = line.strip().split("|")
                if ticket_info[0] == username:
                    count +=1
                    user_tickets.append({
                        "ticket": count,
                        "row": int(ticket_info[1]),
                        "seat": int(ticket_info[2]),
                        "price": int(ticket_info[3])
                    })
                    
    except IOError:
        file = open("ticket_database.txt", "w")
        file.close()
    
    finally:
        return user_tickets

def save_user_info(username, ticket_info):
    """
    This function saves the user's booking information to the text file in the following format:
        alice|1|2|100
        alice|1|3|100
        bob|3|4|80
        charlie|5|6|70
    where each line represents the information for one user, and the fields within each line are separated by | 
    the fields correspond to the username, row number, seat number, and ticket price, respectively.
    if a user books more than 1 ticket, then each ticket will be represented on a separate line in the text file, 
    with each line containing the information for one ticket. 
    The function saves 1 ticket at a time
    
    Parameters
    ----------
    username : str
        Represents the username of the normal user currently logged in.
        Used to associate the booking information with the specific user.
    ticket_info : dict
        A dictionary containing the ticket information, including the row number, seat number, and price. 
        This is formed in the book_ticket function
    
    Returns
    -------
    None
    """
    try:
        with open("ticket_database.txt", "a") as file:
            file.write(f"{username}|{ticket_info['row']}|{ticket_info['seat']}|{ticket_info['price']}\n")
    except IOError:
        with open("ticket_database.txt","w") as file:
            file.write(f"{username}|{ticket_info['row']}|{ticket_info['seat']}|{ticket_info['price']}\n")

        

    
def book_ticket(username):
    """
    This function is responsible for allowing the user to book a ticket.
    It uses the provided username to identify the user who is booking the ticket.
    The user is prompted to enter the row and seat number for the ticket they want to book.
    The price is then displayed, and the user is asked to confirm their choice
    After confirming the choice, the booking is recorded.

        ticket_info = {"row": 1, "seat": 2, "price": 100}
    
    Parameters
    ----------
    username : str
        Represents the username of the normal user currently logged in.
        Used to add bookings for the specific user.
    
    Returns
    -------
    None. 
    """
    while True:
        print()
        row = int(input("Enter row number:  "))
        seat = int(input("Enter seat number: "))
        try:
            if row < 1 or row > 7:
                raise ValueError("Invalid row number. Please choose a row between 1 and 7.")
                
            max_seats = {1: 8, 2: 10, 3: 12, 4: 14, 5: 16, 6: 18, 7: 20}
            max_seat = max_seats[row]
                
            if seat < 1 or seat > max_seat:
                raise ValueError(f"Invalid seat number for the selected row. Please choose a seat number between 1 and {max_seat}.")
        
            if row == 1:
                price = 100
            elif row == 2:
                price = 80
            elif row in [3, 4]:
                price = 70
            elif row == 5:
                price = 60
            elif row == 6:
                price = 40
            elif row == 7:
                price = 20
            
            if ticket_found(row, seat):
                raise ValueError("Sorry, that seat is already booked. Please select another seat.")
        
            print("This ticket is £", price)
        
            purchase = input("Do you want to confirm your purchase? (y/n):   ")
            if purchase.lower() == 'y':
                ticket_info = {"row":row, "seat":seat, "price":price} 
                save_user_info(username, ticket_info)
                print("...")
                print("Booking successful.\n")
                break
            elif purchase.lower() == 'n':
                print("Your purchase has been cancelled.")
                print()
            else:
                print("Invalid input.")
        
        except ValueError as e:
            print(e)
        
def ticket_found(row_number, seat):
    """
    Check if a ticket exists in the ticket database for the specified row and seat.
    
    Parameters
    ----------
    row_number : int
        The row number of the seat to check.
    seat : int
        The seat number to check.
        
    Returns
    -------
    bool
        True if a ticket exists for the specified row and seat, False otherwise.
    """
    try:
        with open("ticket_database.txt", "r") as file:
            for line in file:
                ticket_info = line.strip().split("|")
                if int(ticket_info[1]) == row_number and int(ticket_info[2]) == seat:
                    return True                    
            return False
    except IOError:
        with open("ticket_database.txt", "w") as file:
            # file is empty so ticket not found. return false
            return False

def cancel_ticket(username):
    """
    This function handles the cancellation of tickets by the user.
    It utilizes the provided username to access and manipulate the user's booking history.
    The user is prompted to select the ticket they want to cancel.
    After confirming the cancellation, the ticket is removed from the booking history.
    
    Parameters
    ----------
    username : str
        Represents the username of the normal user currently logged in.
        Used to access and manipulate the user's booking history.
    
    Returns
    -------
    None. 
    """
    line_to_delete = None
    user_tickets = load_user_info(username)
    tickets_available = show_ticket(user_tickets)
    if tickets_available:
        cancelled = False
        while not cancelled:
            ticket_to_cancel = int(input("Please enter the ticket number that you want to cancel: \n"))
            for ticket in user_tickets:
                if ticket_to_cancel == ticket["ticket"]:
                    with open("ticket_database.txt", "r") as file:
                        for line in file:
                            name, row_number, seat, price = line.split("|")
                            if int(row_number) == ticket["row"] and int(seat) == ticket["seat"]:
                                line_to_delete = line.strip("\n")
                        file.seek(0)
                        lines = file.readlines()  
                    with open("ticket_database.txt", "w") as file:
                        for line in lines:
                            if line.strip("\n") != line_to_delete:
                                file.write(line)
                    if line_to_delete:
                        cancelled = True
                        print("Ticket cancelled successfully!\n")
                        break
            if not cancelled:
                print("Please enter a valid ticket number: \n")
                            
    else:
        print("No tickets are available for cancellation.\n")

def show_ticket(user_tickets):
    """
    This function displays the tickets booked by the user.
    It uses the provided username to access the user's booking history.
    The function retrieves the booked tickets and displays them in the following format:
        Ticket 1
        Row: 3
        Seat: 8
        Price: £70
    
    Parameters
    ----------
    user_tickets : list
        list of dictionaries, where each dictionary represents one of the user's booked tickets. 
        Each dictionary contains the ticket information, including the ticket number, row number, seat number, and price    
    
    Returns
    -------
    True
        if the user has one or more tickets booked
    False
        if the user has no tickets booked
    """
    if len(user_tickets) >= 1:
        for ticket in user_tickets:
            ticket_num,row,seat,price = ticket["ticket"],ticket["row"],ticket['seat'],ticket["price"]
            print(f"Ticket {ticket_num}:\n")
            print(f"Row: {row}\n")
            print(f"Seat: {seat}\n")
            print(f"Price: £{price}")
            print("_ _ _ _ _ _ _ _ _ _\n")
        return True
    
    else:
        print("You have no tickets booked at the moment.\n")
        return False

def display_theatre(username, mode):
    """

    This function displays the theatre layout based on the specified mode.
    In 'book' mode (mode 'b'), it shows the current booking status for the theatre,
    marking all the already booked seats with the symbol 'X'.
    
    i.e. :
        
     _ _ _ _ _ _ x _ _ _ _ _ _ _ _ _ _ _ _ _
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x _ _
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           _ _ _ _ _ x _ _ _ _ _ _ _ _
             _ _ _ _ _ _ _ x _ _ _ _
               _ _ _ _ _ _ _ _ _ _
                 _ _ _ _ _ _ _ _
                 
    In 'cancel' mode (mode 'c'), it displays the theatre layout with only the seats
    booked by the user marked with the symbol 'B'.
    
    i.e. :
        
     _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
       _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
         _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
           _ _ _ _ _ B _ _ _ _ _ _ _ _
             _ _ _ _ _ _ _ B _ _ _ _
               _ _ _ _ _ _ _ _ _ _
                 _ _ _ _ _ _ _ _
    
    Parameters
    ----------
    username : str
        Represents the username of the normal user currently logged in.
        Used to access user's booking data i.e., seat coordinates in 'cancel' mode.
        This parameter is ONLY required in mode 'c', as mode 'b' displays the same saved layout for every user.
    mode : str
        Specifies the mode in which the theatre layout should be displayed.
        'b' for book mode (showing all booked seats), 'c' for cancel mode (showing only user's booked seats).
        Raises ValueError if mode is not 'b' or 'c'.
    
    Returns
    -------
    None.

    """
    theatre = {
        7: ['_'] * 20,
        6: ['_'] * 18,
        5: ['_'] * 16,
        4: ['_'] * 14,
        3: ['_'] * 12,
        2: ['_'] * 10,
        1: ['_'] * 8
    }
    try:
        if mode in ["b","c"]:
            if mode == "b":
                with open("ticket_database.txt", "r") as file:    
                    for line in file:
                        name, row_number, seat, price = line.split("|")
                        theatre[int(row_number)][int(seat) - 1] = 'x'
            elif mode == "c":
                with open("ticket_database.txt", "r") as file: 
                    for line in file:
                        name, row_number, seat, price = line.split("|")
                        if name == username:
                            theatre[int(row_number)][int(seat) - 1] = 'B'
        else:
            raise ValueError("Inappropriate argument value for mode")
    except ValueError as e:
        print(e)
    
    except IOError:
        with open("ticket_database.txt", "w"):
            pass
        
    for row in theatre.keys():
        layout = ' '.join(theatre[row])
        indentation = (7 - row) * 2  # Calculate indentation based on row number
        print(" " * indentation + layout)
    print()
    














    