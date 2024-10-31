def menu():
    online = True
    while online:
        print()
        print("Menu:")
        print("1. View Ticketing Status")
        print("2. Cancel Ticket")
        print("3. Reset")
        print("4. Quit")
        choice = int(input("Enter your choice (1-4): "))
        print()
        
        if choice == 1:
            print("Ticketing Status:")
            print()
            display_theatre()
            print()
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
            print("Cancel Ticket:")
            display_theatre()
            print()
            cancel_ticket()
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
            reset_tickets()
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


def display_theatre():
    """
    This function displays the current ticketing status of the theatre.
    It visualises the theatre layout and marks all the bought tickets with the symbol 'x'.
    
   i.e. :
       
    _ _ _ _ _ _ x _ _ _ _ _ _ _ _ _ _ _ _ _
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x _ _
        _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
          _ _ _ _ _ x _ _ _ _ _ _ _ _
            _ _ _ _ _ _ _ x _ _ _ _
              _ _ _ _ _ _ _ _ _ _
                _ _ _ _ _ _ _ _
     
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
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
        with open("ticket_database.txt", "r") as file:
            for line in file:
                name, row_number, seat, price = line.split("|")
                row_number = int(row_number)
                seat = int(seat)
                
                row = theatre[row_number]
                row[seat - 1] = 'x'
    except IOError:
        with open("ticket_database.txt", "w") as file:
            pass
        
    for row in theatre.keys():
        layout = ' '.join(theatre[row])
        indentation = (7 - row) * 2  # Calculate indentation based on row number
        print(" " * indentation + layout)

        
        


def display_ticket_info(row_number, seat):
    """
    This function is used to search for seat information in the theatre, and if it exists, to display it in the following format:
        Row: 3
        Seat: 8
        Price: £70
        
    It takes seat information as input and searches for the corresponding ticket details.
    The function returns True if a ticket exists, otherwise, it returns False.
    
    Parameters
    ----------
    seat_info : str
        A string containing seat information in the format 'row|seat'. ("2|3")
        used to access the booking history
    Returns
    -------
    True or False
        True if the seat is booked.
        False if the seat is not booked.
    """
    try:    
        with open("ticket_database.txt", "r") as file:
            for line in file:
                name, user_row_number, user_seat, price = line.split("|")
                if user_row_number == row_number and user_seat == seat:
                    print(f"Row:   {row_number}")
                    print(f"Seat:  {seat}")
                    print(f"Price: {price}")
                    return True
                else:
                    return False
                    print("This seat has not been booked.")
    except IOError:
        with open("ticket_database.txt", "w") as file:
            pass
        print("This seat has not been booked. ")
        return False

def cancel_ticket():
    """
    This function allows the admin to cancel a booked ticket.
    It utilises the provided seat_info to access and manipulate the text file.
    Once found, the ticket is removed from the booking history.
    
    Parameters
    ----------
    seat_info : str
        A string containing seat information in the format 'row|seat'. ("2|3")
        Used to access and manipulate the booking history.
    
    Returns
    -------
    None
    """

    line_to_delete = None
    with open("ticket_database.txt","r") as file:
        if file.read(1):
            tickets_available = True
        else:
            tickets_available = False
    
    if tickets_available:
        cancelled = False
        while not cancelled:
            print("Please enter the row and seat number of the ticket you want to cancel:")
            row = int(input("Row:  "))
            seat = int(input("Seat: "))
            with open("ticket_database.txt", "r") as file:
                for line in file:
                    name, user_row_number, user_seat, price = line.split("|")
                    if int(user_row_number) == row and int(user_seat) == seat:
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
                print("Invalid row/seat number, ticket not found. \n")
                            
    else:
        print("No tickets are available for cancellation.\n")
        


def reset_tickets():
    """
    This function resets all the booked tickets in the theatre.
    All the booked tickets are cancelled, and the text file is cleared.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    with open("ticket_database.txt", "w") as file:
        pass  # Using pass to do nothing inside the block
    print("All tickets have been reset successfully.")
