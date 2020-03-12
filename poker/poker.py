map_number = {'2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              '10': 10,
              'J': 11,
              'Q': 12,
              'K': 13,
              'A': 14}

def best_hands(hands):
    scores_hands = {hand: get_hand_value(hand) for hand in hands}
    scores = list(sorted((scores_hands[hand] for hand in scores_hands), reverse=True))
    return [hand for hand in scores_hands if scores_hands[hand] == scores[0]]


def get_hand_value(hand):
    hand = parse_hand(hand)
    if is_straight(hand) and is_flush(hand):
        score = (8, is_straight(hand))
    elif is_n_of_a_kind(hand, 4):
        score = (7, is_n_of_a_kind(hand, 4))
    elif is_full_house(hand):
        score = (6, *is_full_house(hand))
    elif is_flush(hand):
        score = (5, is_flush(hand))
    elif is_straight(hand):
        score = (4, is_straight(hand))
    elif is_n_of_a_kind(hand, 3):
        score = (3, is_n_of_a_kind(hand, 3))
    elif is_two_pair(hand):
        score = (2, *is_two_pair(hand))
    elif is_n_of_a_kind(hand, 2):
        score = (1, is_n_of_a_kind(hand, 2))
    else:
        score = (0, *[e[0] for e in hand[-1::-1]])
    return score


def parse_hand(hand):
    hand = hand.split(' ')
    return sorted([(map_number[card[:-1]], card[-1]) for card in hand])


def is_two_pair(hand):
    if (same_suit(hand[:2]) and same_suit(hand[2:4])):
        return hand[2][0], hand[0][0], hand[4][0]
    if (same_suit(hand[:2]) and same_suit(hand[3:5])):
        return hand[3][0], hand[0][0], hand[2][0]
    if (same_suit(hand[1:3]) and same_suit(hand[3:5])):
        return hand[3][0], hand[1][0], hand[0][0]
    return 0


def is_straight(hand):
    if hand[-1][0] != 14:
        return _is_straight(hand)
    else:
        low_hand = hand.copy()
        low_hand[-1] = (1, hand[-1][1])
        low_hand = sorted(low_hand)
        return _is_straight(hand) or _is_straight(low_hand)


def _is_straight(hand):
    current = hand[0][0]-1
    for card in hand:
        if card[0] != current + 1:
            return 0
        current = card[0]
    return hand[-1][0]

def is_full_house(hand):
    if (same_suit(hand[:3]) and same_suit(hand[3:])):
        return hand[2][0], hand[3][0]
    if (same_suit(hand[:2]) and same_suit(hand[2:])):
        return hand[2][0], hand[1][0]
    return 0

def is_flush(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return 0
    return hand[-1][0]


def is_n_of_a_kind(hand, n):
    for i in range(len(hand)-n+1):
        if same_suit(hand[i:i+n]):
            n_kind = hand[i:i+n]
            high_cards = hand.copy()
            for card in n_kind:
                high_cards.remove(card)
            high_cards = sorted(high_cards)
            return (hand[i][0], *[card[0] for card in high_cards])
    return 0


def same_suit(cards):
    value = cards[0][0]
    for card in cards:
        if card[0] != value:
            return False
    return True


def main():
    hands = [
            "3S 3H 2S 3D 3C",
            "3S 3H 4S 3D 3C",
    ]
    print(best_hands(hands))


if __name__ == '__main__':
    main()
