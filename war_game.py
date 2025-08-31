import random

# Create a standard deck (just values, ignoring suits for simplicity)
deck = list(range(2, 15)) * 4   # 2–14 (where 11=Jack, 12=Queen, 13=King, 14=Ace)

# Shuffle deck
random.shuffle(deck)

# Split into two players
player1 = deck[:26]
player2 = deck[26:]
