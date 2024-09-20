import random
from config import REEL_STRUCTURE, SYMBOLS, PAYOUT, FREQUENCY_TABLE


class SlotMachine:
    def __init__(self, reel_structure, symbol, payout, frequency_table):
        self.reel_structure = REEL_STRUCTURE
        self.symbols = SYMBOLS
        self.payout = PAYOUT
        self.frequency_table = FREQUENCY_TABLE
        self.jackpot_count = 0


    def spin_reels(self):
        """
        Spins the reels and fill them based on symbol frequency
        """
        for i in range(len(self.reel_structure)):
            for j in range(len(self.reel_structure[i])):
                if j == 0:
                    self.reel_structure[i][j] = random.choices(self.symbols, self.frequency_table["reel1"])[0]
                elif j == 1:
                    self.reel_structure[i][j] = random.choices(self.symbols, self.frequency_table["reel2"])[0]
                elif j == 2:
                    self.reel_structure[i][j] = random.choices(self.symbols, self.frequency_table["reel3"])[0]

        return self.reel_structure


    def display_reels(self):
        """
        display the slot machine grid
        """
        for i, row in enumerate(self.reel_structure):
            if i == 1:
                print(f"-> {row} <-") # highlight middle value
                continue
            print(f"   {row}")


    def calculate_payout(self):
        """
        Calculate the payout of middle row of slot machine
        """
        middle_row = tuple(self.reel_structure[1])
        total_payout = 0

        # cheeck if all symbol are different
        if len(set(middle_row)) == len(middle_row):
            return total_payout

        # check jackpot
        if middle_row == ('7', '7', '7'):
            print("**** JACKPOT!!! Grand-Payout ****")
            total_payout += self.payout[('7', '7', '7')]

        # check if three of a kind
        if middle_row in self.payout:
            total_payout += self.payout[middle_row]
            print("\n**** WIN ****\n")

        # check two of a kind
        for i in range(len(middle_row) - 1):
            two_kind = (middle_row[i], middle_row[i+1])
            if two_kind in self.payout:
                total_payout += self.payout[two_kind]

        # check for single symbol
        for symbol in middle_row:
            if (symbol, ) in self.payout:
                total_payout += self.payout[(symbol, )]

        return total_payout
