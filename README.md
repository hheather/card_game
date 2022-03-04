# How to run
1. Requires python 3.9
2. From project root, run python3 -m venv ./venv
3. Activate venv with: source venv/bin/activate
4. Run python3 -m pip install -r requirements.txt
5. Run card_game/src/card_game/main.py to have an exciting game of cards!

# How I completed the task
1. I outlined each component of the card game which I believe to be: suit, rank, card and deck.
2. Suit and rank will be used to create each card.
3. Cards will then be generated using all combinations of suits and ranks.
4. Cards will collectively belong to a deck.
5. Deck will have the functionality of being able to shuffle and draw it's cards.
   - Lists are straightforward to shuffle and draw from using the built in random module.
6. I then implemented the tests using pytest fixtures which represented much simpler versions of each class
   - During testing I realised the random.choices() function can return duplicates so swapped this with random.sample()
