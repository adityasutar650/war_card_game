import random

# Create a standard deck (just values, ignoring suits for simplicity)
deck = list(range(2, 15)) * 4   # 2–14 (where 11=Jack, 12=Queen, 13=King, 14=Ace)

# Shuffle deck
random.shuffle(deck)

# Split into two players
player1 = deck[:26]
player2 = deck[26:]

round_num = 0
# if game doesnt end in 10K rounds, declare winner based on number of cards

while ((player1 and player2) and (round_num<10000)):  # while both players have cards
    round_num += 1
    card1 = player1.pop(0)   # take top card
    card2 = player2.pop(0)

    print(f"Round {round_num}: Player 1 plays {card1}, Player 2 plays {card2}")

    if card1 > card2:
        player1.extend([card1, card2])   # winner gets both cards
        print("Player 1 wins the round\n")
    elif card2 > card1:
        player2.extend([card1, card2])
        print("Player 2 wins the round\n")
    else:
        print("Tie! Both cards discarded\n")
        # do nothing (cards are discarded)

    print(f"Player 1 has {len(player1)} cards, Player 2 has {len(player2)} cards\n")


# Determine winner
if len(player1) > len(player2):
    print("🎉 Player 1 wins the game!")
elif len(player2) > len(player1):
    print("🎉 Player 2 wins the game!")
else:
    print("It's a draw!")
        # do nothing (cards are discarded)

