import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}
symbol_values = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symb = columns[0][line]
        for col in columns:
            if symb != col[line]:
                break
        else:
            winnings += values[symb] * bet
            winning_lines.append(line)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbolCount in symbols.items():
        for _ in range(symbolCount):
            all_symbols.append(symbol)
    #[A,A,B,B,B,B,C,C,C,C,C,C,D,D,D,D,D,D]

    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:] #copy of all symbols and not refrence
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column)-1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposite? ₹")
        if amount.isdigit() : # amount.isdigit() is used to check : we provide string and check if all characters are digit or not
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Please enter amount greater than 0.")
        else:
            print("Please enter number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-"+str(MAX_LINES)+") : ")
        if lines.isdigit() : 
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter lines from 1 to "+str(MAX_LINES)+".")
        else:
            print("Please enter number.")
    return lines    

def get_bet_amount():
    while True:
        bet_amount = input("Enter amount you would like to bet on each line : ")
        if bet_amount.isdigit() : 
            bet_amount = int(bet_amount)

            if MIN_BET < bet_amount <= MAX_BET:
                break
            else:
                print(f"Please enter amout between ₹{MIN_BET} and ₹{MAX_BET}.")                       
        else:
            print("Please enter number.")
    return bet_amount  

def play(balance):
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet_amount()
        total_bet = bet_amount*lines

        if total_bet > balance:
                print(f"Insufficient balance your current balance is : ₹{balance}")
        else:
            break

    print(f"You are betting ₹{bet_amount} on {lines} lines your total bet amount is ₹{total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print("====================")
    print(slots)
    print("====================")

    print_slot_machine(slots)
    print()

    winnings, winning_lines = check_winnings(slots,lines,bet_amount,symbol_values)
    if winnings > 0:
        print(f"You won ${winnings}.")
        print(f"You won on lines:", *winning_lines)
    else:
        print("sorry you didnt win anything")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ₹{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break

        balance += play(balance)
    print(f"You left with ${balance}")



main()


    