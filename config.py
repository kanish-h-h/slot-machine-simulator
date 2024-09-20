# Configuration Constants

REEL_STRUCTURE = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]

SYMBOLS = ['1', '2', '3', '4', '7']

PAYOUT = {
    ('1', '1', '1'): 5,     # Three cherries
    ('2', '2', '2'): 10,    # Three lemons
    ('3', '3', '3'): 20,    # Three oranges
    ('4', '4', '4'): 40,    # Three bells
    ('7', '7', '7'): 1000,  # JACKPOT
    ('1', '1'): 1,          # Two cherries
    ('2', '2'): 2,          # Two lemons
    ('3', '3'): 5,          # Two oranges
    ('4', '4'): 10,         # Two bells
    ('1',): 0.5,            # One cherry
    ('2',): 1,              # One lemon
    ('3',): 2,              # One orange
    ('4',): 5               # One bell
}

FREQUENCY_TABLE = {
    "reel1": [10, 8, 6, 4, 1],
    "reel2": [12, 7, 5, 3, 1],
    "reel3": [9, 7, 6, 5, 1]
    }
