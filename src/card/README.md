### Procedural thinking
What steps do I need to perform?
- shuffle cards
- deal cards to players
- compare card values
- determine winner

### OOP thinking
What entities exist in this problem?
- Cards (things that have rank/suit)
- Deck (thing that holds/manages cards)
- Player (things that receive cards)
- Game (thing that orchestrates iterations)


What responsibilities does each entity have?

Read the problem and circle nouns:

"Each `player` draws one `card` from a shuffled `deck`.
The `player` whose `card` has the highest `rank` wins the `round`."

player
- draw one card

Game
- players
- deck
- play
- compare rank