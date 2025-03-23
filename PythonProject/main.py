
import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

    return [random.choice(symbols) for _  in range (3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 7
    return 0

def main():
    balance = 100

    print("         ****************")
    print("Symbols: |🍒|🍉|🍋|🔔|⭐")
    print("         ****************")

    while balance > 0:
        print("Current Balance: R" + str(balance))

        bet = input("Place your bet amount: R")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)


        if payout > 0:
            print(f"You won!, R{payout}")
            balance+=payout
        else:
            print("You lose!")

        if balance == 0:
            print("Game over! You ran out of balance.")
            balance += payout

if __name__ == '__main__':
        main()