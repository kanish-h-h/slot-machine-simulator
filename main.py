from config import REEL_STRUCTURE, SYMBOLS, FREQUENCY_TABLE, PAYOUT
from slot_machine import SlotMachine
from player import Player
from game import Game


def main():
    # create a player
    initial_amount = get_betting_amount()
    player = Player(initial_amount)

    # Create a slot machine instance
    slot_machine = SlotMachine(REEL_STRUCTURE, SYMBOLS, PAYOUT, FREQUENCY_TABLE)

    # Create a game instance
    game = Game(player, slot_machine)

    # Ask for the number of spins
    num_spins = int(input("Enter the number of spins: "))

    # Start the game
    game.play_round(num_spins)


def get_betting_amount():
    """
    Prompt the user for an initial betting get_betting_amount
    """
    while True:
        try:
            amount = float(input("Enter your betting amount (minimum $10): $"))
            if amount < 10:
                print("Amount must be at least $10.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value")


if __name__ == "__main__":
    main()
