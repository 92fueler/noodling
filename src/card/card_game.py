"""
Each player draws one card from a shuffled deck.
The player whose card has the highest rank wins the round.


"""

from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional
import random


# ------------------------------
# Enums for Rank and Suit
# ------------------------------


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

    def __str__(self) -> str:
        return self.name.capitalize()


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14  # Ace high

    def __str__(self) -> str:
        # For friendlier printing
        if self.value <= 10:
            return str(self.value)
        return self.name.capitalize()


# ------------------------------
# Card, Deck, Player
# ------------------------------


@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        self._cards: List[Card] = [Card(rank, suit) for suit in Suit for rank in Rank]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def deal_one(self) -> Optional[Card]:
        if not self._cards:
            return None
        return self._cards.pop()

    def cards_left(self) -> int:
        return len(self._cards)


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand: List[Card] = []

    def receive_card(self, card: Card) -> None:
        self.hand.append(card)

    def show_hand(self) -> List[Card]:
        return list(self.hand)

    def reset_hand(self) -> None:
        self.hand.clear()

    def __repr__(self) -> str:
        return f"Player({self.name})"


# ------------------------------
# Simple Game: High Card Wins
# ------------------------------


class HighCardGame:
    def __init__(self, player_names: List[str]) -> None:
        if len(player_names) < 2:
            raise ValueError("Need at least 2 players")

        self.players: List[Player] = [Player(name) for name in player_names]
        self.deck = Deck()

    def play_round(self) -> Optional[Player]:
        """
        Each player draws 1 card.
        The player with the highest card wins the round.
        Returns the winning Player, or None on a tie.
        """
        # Clear old hands
        for p in self.players:
            p.reset_hand()

        # Deal one card to each player
        for p in self.players:
            card = self.deck.deal_one()
            if card is None:
                print("Deck is out of cards, cannot play round.")
                return None
            p.receive_card(card)

        # Show hands
        print("\n--- New Round ---")
        for p in self.players:
            print(f"{p.name} drew: {p.show_hand()[0]}")

        # Determine winner
        best_player: Optional[Player] = None
        best_card: Optional[Card] = None
        is_tie = False

        for p in self.players:
            card = p.show_hand()[0]
            if best_card is None or card.rank.value > best_card.rank.value:
                best_card = card
                best_player = p
                is_tie = False
            elif card.rank.value == best_card.rank.value:
                # Tie on rank – for simplicity, we ignore suit tiebreakers
                is_tie = True

        if is_tie or best_player is None:
            print("It's a tie!")
            return None

        print(f"Winner: {best_player.name} with {best_card}")
        return best_player


# ------------------------------
# Small demo
# ------------------------------

if __name__ == "__main__":
    game = HighCardGame(["Alice", "Bob", "Charlie"])

    # Play a few rounds
    for _ in range(5):
        game.play_round()
        print(f"Cards left in deck: {game.deck.cards_left()}")
