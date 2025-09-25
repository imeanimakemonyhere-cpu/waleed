import random   # module for randomness

def spin_row(symbols):
    """Return a random row of 3 symbols"""
    return [random.choice(symbols) for _ in range(3)]

def main():
    balance = 100
    symbols = ["🍒", "🍌", "🍊", "⭐"]

    print("Welcome to Python Slots!")
    print("You start with $100.\n")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        # check if bet is a number
        if not bet.isdigit():
            print("Please enter a valid number.\n")
            continue

        bet = int(bet)

        # check bet conditions
        if bet > balance:
            print("Insufficient funds, try again.\n")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.\n")
            continue

        # subtract bet
        balance -= bet

        # spin the slot machine
        row = spin_row(symbols)
        print(" | ".join(row))

        # simple payout rule: all 3 match → win double
        if row[0] == row[1] == row[2]:
            win = bet * 2
            balance += win
            print(f"🎉 Jackpot! You won ${win}!\n")
        else:
            print("No match, better luck next time!\n")

    print("Game over! You ran out of money.")

if __name__ == "__main__":
    main()






        