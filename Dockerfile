FROM python:latest

RUN pip install pytz

WORKDIR /code

Copy csv_games_reader.py .

CMD ["python", "csv_games_reader.py"]
