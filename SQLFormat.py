#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Format SQL OUTPUT

"""


from pandas import DataFrame
from sqlite3 import Connection

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