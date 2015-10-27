#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
import random
import pickle
import datetime
import sys

__author__ = "rpalmaotero"


class LogsGenerator:

    N = 150000

    def __init__(self):
        self.ip_set = set()
        self.urls_sample = []
        self.statuses_sample = []
        self.generated_logs = []

    def generate(self):
        print("[LOG] Generando {} logs. Puede tardar un poco...".format(
            self.N
        ))

        self.populate_ip_set()
        self.populate_urls_sample()
        self.populate_statuses_sample()

        for i in range(self.N):
            self.generate_single_log()

            print("Porcentaje progreso: {}%".format(
                round((100 * i)/self.N)), end="\r")
            sys.stdout.flush()

        self.generated_logs.sort(key=lambda l: l[1].timestamp())
        self.generated_logs = list(map(
            lambda l: l[0],
            self.generated_logs
        ))

    def populate_ip_set(self):
        for i in range(5000):
            ip = ".".join(map(str, [random.randint(0, 255) for _ in range(4)]))
            self.ip_set.update((ip,))

    def populate_urls_sample(self):
        with open("urls_sample", "rb") as f:
            self.urls_sample = [val for val, n in pickle.load(f)
                                for _ in range(n)]

    def populate_statuses_sample(self):
        with open("statuses_sample", "rb") as f:
            self.statuses_sample = [val for val, n in pickle.load(f)
                                    for _ in range(n)]

    def generate_single_log(self):
        # IP
        ip = random.choice(tuple(self.ip_set))

        # Datetime
        beginning = datetime.datetime.now() - datetime.timedelta(days=7)
        date_time = beginning + datetime.timedelta(
            seconds=random.randint(1, 604800))

        # URL
        url = random.choice(self.urls_sample)

        # Status
        status = random.choice(self.statuses_sample)

        # Bytes
        byts = round(random.gauss(300, 100))

        self.generated_logs.append((
            "{} - - [{} -0400] \"{}\" {} {}".format(
                ip, date_time.strftime("%d/%b/%Y:%H:%M:%S"), url, status, byts
            ), date_time
        ))

    def dump(self):
        with open("nasa_logs_week.txt", "w") as f:
            f.write("\n".join(self.generated_logs))


if __name__ == '__main__':
    logs_generator = LogsGenerator()
    logs_generator.generate()
    logs_generator.dump()
