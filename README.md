# How to run
1. Requires python 3.9
2. From project root, run `python3 -m venv ./venv`
3. Activate venv with: `source venv/bin/activate`
4. Run `python3 -m pip install -r requirements.txt`
5. Run card_game/src/card_game/main.py to have an exciting game of cards!

# How to test
1. Follow steps 2, 3 and 4 as above
2. Run `pip install -e .[tests]`
3. Run `pytest`

# How I completed the task
1. I outlined each component of the card game which I believe to be: suit, rank, card and deck.
2. Suit and rank will be used to create each card.
3. Cards will then be generated using all combinations of suits and ranks.
4. Cards will collectively belong to a deck.
5. Deck will have the functionality of being able to shuffle and draw it's cards.
   - Lists are straightforward to shuffle and draw from using the built in random module.
6. I then implemented the tests using pytest fixtures which represented much simpler versions of each class
   - During testing I realised the random.choices() function can return duplicates so swapped this with random.sample()
7. I wrote the Dockerfile so that it uses the python 3.9 image, copies the requirements across and installs them,
    copies the entire card_game dir across, before setting /opt as the WORKDIR and running the module from there.
8. For the github actions, I'd never used these before but tried to get my head around them:
    - build-and-push-docker-image: This action is performed on the "release" branch, tested and appears to work
    - run-pytests: Involves some initial pip installs then running the `pytest` command to view output

# How this would be run in a production environment:
1. This application is packaged as a Dockerfile - the image of which can be used to run in a container,
 and deployed, for example within a Kubernetes cluster into production.
2. Logs can be taken from the container / the cluster / cloud platform and monitored to gather 
    metrics to help determine the health of the application. For example, if for a period of time logs are not 
    being outputted - this may indicate the application is no longer running.
3. Other metrics could be collected including: CPU utilization, memory and disk space to monitor
    the overall health of the container, and compared against the historic trend to determine unusual patterns / possible issues.