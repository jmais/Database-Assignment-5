import sqlite3


class Sightings:
    def __init__(self):
        self.conn = sqlite3.connect('flowers2019.db')
        self.cur = self.conn.cursor()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def getTop10(self,name):
        rows = self.cur.execute("SELECT * from SIGHTINGS Where SIGHTINGS.NAME =? ORDER BY SIGHTINGS.sighted DESC LIMIT 10",(name,))
        return rows



