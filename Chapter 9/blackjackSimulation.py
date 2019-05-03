#Blackjack Simulation


import random


def create_deck():
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    return deck


def deal_cards_1(deck, hand_value_1):
    for count in range(1):
        card = random.choice(list(deck.keys()))
        value = deck.pop(card)
        print('Player 1')
        print(card)
        if value == 1:
            if hand_value_1 + 11 <= 21:
                hand_value_1 += 11
            else:
                hand_value_1 += value
        else:
            hand_value_1 += value
        print('Hand Value:', hand_value_1)
    return hand_value_1


def deal_cards_2(deck, hand_value_2):
    for count in range(1):
        card = random.choice(list(deck.keys()))
        value = deck.pop(card)
        print('Player 2')
        print(card)
        if value == 1:
            if hand_value_2 + 11 <= 21:
                hand_value_2 += 11
            else:
                hand_value_2 += value
        else:
            hand_value_2 += value
        print('Hand Value:', hand_value_2)
    return hand_value_2


def main():
    deck = create_deck()
    value_1 = 0
    value_2 = 0
    value_1 = deal_cards_1(deck, value_1)
    value_2 = deal_cards_2(deck, value_2)
    while value_1 < 21 and value_2 < 21:
        value_1 = deal_cards_1(deck, value_1)
        value_2 = deal_cards_2(deck, value_2)
    if value_1 > 21 and value_2 < 21:
        print('Player 2 wins!!')
    elif value_1 < 21 and value_2 > 21:
        print('Player 1 wins')
    elif value_1 > 21 and value_2 > 21:
        print('Both the players lose.')
    elif value_1 == 21 and value_2 == 21:
        print('It was a tie.')
    elif value_1 == 21:
        print('Player 1 wins!!!')
    elif value_2 == 21:
        print('Player 2 wins!!!')


main()

