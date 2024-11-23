import random

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0
    aces = 0

    # Legger til verdien for hvert kort, teller antall ace
    for card in hand:
        card_value = get_card_value(card)
        hand_value += card_value
        if "Ace" in card:
            aces += 1

    # Justerer verdien av ace fra 11 til 1 om nødvendig for å unngå å buste
    while hand_value > 21 and aces:
        hand_value -= 10
        aces -= 1

    return hand_value