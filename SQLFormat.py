#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Format SQL OUTPUT

"""


from pandas import DataFrame
import sqlite3

class SQLFormat(DataFrame):
    def __init__(self, connection):
        """Init object
        connection: SQLite connection
        """
        super().__init__()
        self.cursor = connection.cursor()