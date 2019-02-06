#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Format SQL OUTPUT

"""

import pandas as pd
from pandas import DataFrame
from sqlite3 import Connection
from chardet import detect

# set display max_colwidth
pd.set_option("display.max_colwidth", 100)

class SQLFormat(Connection):
    def __init__(self, connection):
        """Init object
        connection: SQLite connection
        """
        super().__init__
        self.connection = connection
        self.cursor = connection.cursor()
    
    def query(self, query_string):
        """Query Information
        Query the database, and get the column names

        Parameters:
        ------------
        query_string: string
            SQL query string
        """
        self.connection.text_factory = str

        try:
            result = self.cursor.execute(query_string).fetchall()
        except:
            self.connection.text_factory = bytes
            result = self.cursor.execute(query_string).fetchall()
        
        columns = []
        for column in self.cursor.description:
            columns.append(column[0])
        
        return result, columns

    def format(self, query_string):
        """Format Output
        """
        result, columns = self.query(query_string)

        # store data
        data = dict()
        for i in columns:
            data[i] = []

        for row in result:
            for element, column in zip(row, columns):
                if isinstance(element, bytes):
                    decode_char = element.decode(detect(element)["encoding"])
                    data[column].append(decode_char)
                else:
                    data[column].append(element)
        return pd.DataFrame(data)
                