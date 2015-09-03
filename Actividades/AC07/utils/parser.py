#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
import re
import codecs

__author__ = "rpalmaotero"


class ApacheLogsParser:

    REGEX = '^(\S+) (\S+) (\S+) \[(.*?)] "(.*?)" (\S+) (\S+)$'

    def __init__(self, path):
        self.path = path

    def get_apache_logs(self):
        print("[LOG] Parseando logs... (puede demorarse un poco)")

        with codecs.open(self.path, "r", encoding="utf-8", errors="ignore") \
                as raw_logs:
            logs = []

            for line in raw_logs:
                try:
                    groups = re.match(self.REGEX, line).groups()
                    logs.append(ApacheLog(*groups))
                except AttributeError:
                    pass

            print("[LOG] Parseados {} logs.".format(len(logs)))

            return logs


class ApacheLog:
    def __init__(self, remote, hyphen, user, timestamp, request, status, size):
        self.remote = remote
        self.hyphen = hyphen
        self.user = user
        self.timestamp = timestamp
        self.request = request
        self.status = int(status)
        try:
            self.size = int(size)
        except ValueError:
            self.size = 0
