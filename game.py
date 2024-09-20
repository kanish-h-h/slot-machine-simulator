
class Game:
    def __init__(self, player, slot_machine):
        self.player = player
        self.slot_machine = slot_machine
        self.cost_per_spin = 2
        self.total_bet = 0
        self.total_winning = 0
        self.total_spins = 0
        self.win_count = 0


    def play_round(self, num_spins):
        """
        Spins the slots a specified number of times, one at a time on user input.
        """
        for _ in range(num_spins):
            if not self.player.place_bet(self.cost_per_spin):
                break

            input("\nPress ENTER to spin....")
            reel = self.slot_machine.spin_reels()
            self.slot_machine.display_reels()

            payout = self.slot_machine.calculate_payout()
            self.player.add_winnings(payout)
            self.total_winning += payout
            self.total_bet += self.cost_per_spin
            self.total_spins += 1

            if payout > 0:
                self.win_count += 1

            print(f"\bTotal payout for this spin: {payout}")
            print(f"Player's current balance: ${self.player.get_balance():.2f}")

        self.display_results()


    def display_results(self):
        """
        Display the game results after all spins.
        """
        print("\n--- Game Over ---")
        print(f"Total spins: {self.total_spins}")
        print(f"Total wins: {self.win_count}")
        print(f"Total Jackpot wins: {self.slot_machine.jackpot_count}")
        print(f"Total Bet: ${self.total_bet:.2f}")
        print(f"Total Winnings: ${self.total_winning:.2f}")
        print(f"RTP: {self.calculate_rtp():.2f}%")


    def calculate_rtp(self):
        """
        Calculate the Return to Player (RTP)
        """
        if self.total_bet > 0:
            return (self.total_winning / self.total_bet) * 100
        return 0
