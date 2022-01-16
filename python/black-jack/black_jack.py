"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """
    if card in "JQK":
        return 10
    elif card == 'A':
        return 1

    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise) 
    :return: int - value of the upcoming ace card (either 1 or 11)..
    """
    return 1 if value_of_card(card_one) + value_of_card(card_two) + 11 > 21 else 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    res = 0
    for card in card_one, card_two:
        if card in ('K', 'Q', 'J'):
            res += 10
        elif card == 'A':
            res += 11
        else:
            res += int(card)
    return res == 21
    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
