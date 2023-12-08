import re
from collections import Counter
import random


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

    def __init__(self, cards: list[str], bid: int) -> None:
        self.hand_id = int(random.random() * 1000000000)
        while self.hand_id in Hand.hand_nums:
            self.hand_id = int(random.random() * 1000000000)
        Hand.hand_nums[self.hand_id] = self
        self.cards = cards
        self.cards_sorted = sorted(
            self.cards, key=lambda c: Hand.card_powers[c], reverse=True
        )  # Highest to lowest
        self.cards_counter = Counter(self.cards)
        self.bid = bid
        self.distinction = self.distinction_evaluator()
        self.hand_card_powers = {c: Hand.card_powers[c] for c in self.cards_counter}
        self.hand_total_power = sum(Hand.card_powers[c] for c in self.cards)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            return NotImplemented

        return self.cards == __value.cards

    def __hash__(self) -> int:
        return hash(tuple(self.cards))

    def distinction_evaluator(self) -> str:
        if len(self.cards) != 5:
            raise IncorrectInputError(
                f"Not a valid hand of cards! (len({self.cards}) != 5)"
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
                return "High Card"
            case _:
                raise IncorrectInputError(
                    f"Not a valid hand of cards! (cards_counter = {self.cards_counter})"
                )


def cards_sorter(cards: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(cards, key=lambda tup: Hand.card_powers[tup[0]], reverse=True)


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
        final_hands: list[Hand] = []
        next_to_sort_hands: list[Hand] = hands_of_type
        for i in range(5):
            # If all cards at index i are the same, no point sorting, move on
            if len({h.cards[i] for h in next_to_sort_hands}) == 1:
                continue

            cards_counter = Counter((h.cards[i]) for h in next_to_sort_hands)
            all_cards_at_index_i = [(h.cards[i], h.hand_id) for h in next_to_sort_hands]
            sorted_all_cards_at_index_i = cards_sorter(all_cards_at_index_i)

            temp = []
            for card_tup in sorted_all_cards_at_index_i:
                card = card_tup[0]
                if cards_counter[card] <= 1:  # No multiples
                    temp.append(
                        next_to_sort_hands.pop(
                            next_to_sort_hands.index(Hand.hand_nums[card_tup[-1]])
                        )
                    )
            final_hands = temp + final_hands

            if not next_to_sort_hands:  # exhausted the list
                break

        hands_of_type = final_hands

    rankings[hand_type] = hands_of_type

actual_rankings: list[Hand] = []
for rankings_list in rankings.values():
    actual_rankings.extend(rankings_list)

multiplied_value_final = 0
for hand_rank, hand in enumerate(actual_rankings[::-1]):
    multiplied_value = hand.bid * (hand_rank + 1)
    multiplied_value_final += multiplied_value

print(multiplied_value_final)
