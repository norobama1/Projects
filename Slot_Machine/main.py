import random

MAX_LINES =3
MAX_BETS =100
MIN_BETS =1

ROWS =3
COLS =3

symbol_count = {
   "A": 3,
   "B": 4,
   "C": 5,
   "D": 6,

}

symbol_value = {
   "A": 6,
   "B": 5,
   "C": 4,
   "D": 3,

}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def Deposit():
    while True:
     amount = int(input("Enter the amount you want to deposit: $"))
     if amount >0: 
        break
     else:
         print("Isufficient Amount!!")

    return amount

def get_lines():
    while True:
     lines = int(input(f"Enter the number of lines to bet on 1-{MAX_LINES} "))
     if 1<=lines<=MAX_LINES:
        break
     else:
         print("Enter within the range!!")

    return lines

def get_bet():
    while True:
     bet = int(input("Enter the amount you want to put on each line: $"))
     if MIN_BETS<=bet<=MAX_BETS: 
        break
     else:
         print(f"Amount must be between ${MIN_BETS} - ${MAX_BETS}.")

    return bet

def spin(balance):
    lines =get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = Deposit()
    while True:
       print(f"Your current balance is ${balance}")
       answer = input("Press enter to play (q to quit).")
       if answer == "q":
            break
       balance += spin(balance)

    print(f"You left with ${balance}")

main()