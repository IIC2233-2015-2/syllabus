__author__ = 'ivania'

import json
from collections import defaultdict
start_hour = '23:30'


def read_tweet(tweet, words_frequency, players_frequency, players_names):
    # Implementar
    # Buscar palabras frecuentes
    # Revisar si las palabras corresponden a un jugador
    return words_frequency, players_frequency


def read_tweets_window(start, end, registers, players_names):
    # Implementar
    # Revisar las palabras para cada tweet si está en la ventana de tiempo
    words_frequency = {}
    players_frequency = {}
    # Filtrar palabras infrecuentes

    return words_frequency, players_frequency


def is_in_time_window(hour, start, end):
    # Implementar
    return True


def transform_event_time(minute):
    hour_s, min_s = start_hour.split(':')
    min_s = int(min_s)
    hour_s = int(hour_s)
    if min_s + minute > 59:
        if hour_s + (min_s + minute) / 60 > 23:
            hour_s = int((min_s + minute) / 60 - 1)
        min_s = (min_s + minute) % 60
    else:
        min_s += minute

    return hour_s, min_s


def frequent_words(tweets, events, players_words):
    event_statistics = {}

    for event in events:
        # Implementar
        # Obtener frecuencias de las palabras de la ventana del evento
        words_frequency = {}

        # Cada uno de estos archivos lo pueden utilizar en wordcloud
        with open('Evento{}.txt'.format(minute), 'w+') as file_words:
            for word, frequency in words_frequency.items():
            file_words.write('{}\t{}\n'.format(frequency, word))

    return event_statistics


def load_names_players(players):
    players_names = {}
    # Implementar
    # Crear diccionario para guardar las palabras asociadas a cada uno de los
    # jugadores

    return players_names


if __name__ == "__main__":

    # Crear dict de jugadores
    players_words = load_names_players(players)
    events_statistics = frequent_words(tweets, events, players_words)
