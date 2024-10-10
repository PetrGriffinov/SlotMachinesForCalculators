# Python Slot Machine
import random

def spin_row():
    symbols = ['🍒', '⭐', '🍑', '💦', '🍆']

    return [random.choice(symbols)for _ in range(3)]

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row [0] == '🍒':
            return bet * 2
        elif row[0] == '⭐':
            return bet * 2
        elif row[0] == '🍑':
            return bet * 10
        elif row[0] == '💦':
            return bet * 3
        elif row[0] == '🍆':
            return bet * 5
    elif (row[0] == row[1] != row[2]) or (row[1] == row[2] != row[0]) or (row[0] == row[2] != row[1]):
        return bet * 0.5
    elif row[0] == '🍆':
        if row[1] == '🍑':
            if row[2] == '💦':
                return bet * 69
    
    return 0
        

def main():
    balance = 100

    print("--------------------------------")
    print("🎰Welcome to the Calculator Casino🎰")
    print("--------------------------------")

    while balance > 0:
        print(f"Current balance. ¥{balance}")

        bet = input("Place your bet amount:")
        
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds to place this bet")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")

        balance -= bet

        row = spin_row ()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ¥{payout}")
        else:
            print("You lost! LOSER!")

        balance += payout

        if balance <= 0:
            print("You ran out of money!")
            addBalance = input("How much money would you like to deposit: ")
            if not addBalance.isdigit():
                print("Please enter a valid number!")
                addBalance = input("How much money would you like to deposit: ")
                if not addBalance.isdigit():
                    print("This is your last chance to enter a valid number!")
                    addBalance = input("How much money would you like to deposit: ")
                    if not addBalance.isdigit():
                        print("F*CK OFF!")
                        continue
            addBalance = int(addBalance)
            balance += addBalance

if __name__ == '__main__' :
    main()