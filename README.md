# Python remake of Google Doodle Rise of the Half Moon

## Requirements

```
numpy
```

## How to play
This Python remake is currently text-based (terminal-based). Run the `main.py` file to start the game. Rules:
- Each player starts with 3 cards, each bears a random number between 0 and 7.
- Each player takes turn play a card by entering a number that they have in their hand, then a position number on the board:
  - Board positions are arranged like this:
    - 0 - 1 - 2
    - 3 - 4 - 5
    - 6 - 7 - 8
- Each card value coresponds to a moon phase:
  - 0: New Moon
  - 1: Waxing Crescent
  - 2: First Quarter
  - 3: Waxing Gibbous
  - 4: Full Moon
  - 5: Waning Gibbous
  - 6: Third Quarter
  - 7: Waning Crescent
- Adjacent cards with the same moon phase as your card grant 1 point each.
- Adjacent cards that create a full moon with your card grant 2 points each ($|x-y|=4$).
- If your card fills a moon cycle of length $L \geq 3$, you gains $L$ points.
- Once the board is filled, the player with more points wins.

## To do
- [] Add territory counting at the end of the match.
- [] Add UI and game graphics.
