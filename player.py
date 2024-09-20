
class Player:
    def __init__(self, balance):
        self.balance = balance


    def place_bet(self, amount):
        """
        Deduct the betting amount from the balance
        """
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient Funds!")
            return False


    def add_winnings(self, payout):
        """
        Add winnings to the player's balance
        """
        self.balance += payout


    def get_balance(self):
        return self.balance
