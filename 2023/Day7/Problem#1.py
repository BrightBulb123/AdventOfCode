import random
import re
from collections import Counter

file_name = "2023/Day7/Day7Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


class IncorrectInputError(Exception):
    pass


class SameHandsPassedForComparison(Exception):
    pass


class Hand:
    card_powers = {
        c: p
        for c, p in zip(
            ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"),
            range(14, 1, -1),
        )
    }
    card_distinctions = {
        d: n
        for d, n in zip(
            (
                "Five of a kind",
                "Four of a kind",
                "Full house",
                "Three of a kind",
                "Two pair",
                "One pair",
                "High card",
            ),
            range(7, 0, -1),
        )
    }
    hand_nums = {}
    HAND_LENGTH = 5

    def __init__(self, cards: list[str], bid: int) -> None:
        self.hand_id = int(random.random() * 1000000000)
        while self.hand_id in Hand.hand_nums:
            self.hand_id = int(random.random() * 1000000000)
        Hand.hand_nums[self.hand_id] = self
        self.cards = cards
        self.cards_counter = Counter(self.cards)
        self.bid = bid
        self.distinction = self.distinction_evaluator()
        self.hand_card_powers = [Hand.card_powers[c] for c in self.cards]

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return NotImplemented

        return self.cards == __value.cards

    def __hash__(self) -> int:
        return hash(tuple(self.cards))

    def distinction_evaluator(self) -> str:
        if len(self.cards) != Hand.HAND_LENGTH:
            raise IncorrectInputError(
                f"Not a valid hand of cards! (len({self.cards}) != {Hand.HAND_LENGTH})"
            )
        match len(self.cards_counter):
            case 1:
                return "Five of a kind"
            case 2:
                if self.cards_counter.most_common(1)[0][-1] == 4:
                    return "Four of a kind"
                elif self.cards_counter.most_common(1)[0][-1] == 3:
                    return "Full house"
            case 3:
                if self.cards_counter.most_common(1)[0][-1] == 3:
                    return "Three of a kind"
                most_common_2_counts = (
                    card_info[-1] for card_info in self.cards_counter.most_common(2)
                )
                if len(set(most_common_2_counts)) == 1:
                    return "Two pair"
            case 4:
                return "One pair"
            case 5:
                return "High card"
            case _:
                raise IncorrectInputError(
                    f"Not a valid hand of cards! (cards_counter = {self.cards_counter})"
                )


all_hands: list[Hand] = []
for line in lines:
    hand_str, bid = re.split("\s+", line.strip())
    bid = int(bid)
    hand = Hand(cards=list(hand_str), bid=bid)
    all_hands.append(hand)

rankings: dict[str, list[Hand]] = {}
for hand_type in Hand.card_distinctions:
    hands_of_type = [hand for hand in all_hands if hand.distinction == hand_type]
    if len(hands_of_type) > 1:
        hands_of_type.sort(
            key=lambda h: tuple(h.hand_card_powers[i] for i in range(Hand.HAND_LENGTH)),
            reverse=True,
        )

    rankings[hand_type] = hands_of_type

actual_rankings: list[Hand] = []
for rankings_list in rankings.values():
    actual_rankings.extend(rankings_list)

multiplied_value_final = 0
for hand_rank, hand in enumerate(actual_rankings[::-1]):
    multiplied_value = hand.bid * (hand_rank + 1)
    multiplied_value_final += multiplied_value

print(multiplied_value_final)
