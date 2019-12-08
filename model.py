import sqlite3


class Sightings:
    def __init__(self):
        con = sqlite3.connect('flowers2019.db')
        self.cur = con.cursor()



