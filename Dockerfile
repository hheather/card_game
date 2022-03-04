FROM python:3.9

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /opt/card_game
ADD /src/card_game /opt/card_game

WORKDIR /opt

CMD ["python", "-m", "card_game.main"]
