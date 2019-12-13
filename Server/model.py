import sqlite3


class Sightings:
    def __init__(self):
        self.conn = sqlite3.connect('flowers2019.db')
        self.cur = self.conn.cursor()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def getTop10(self, name):
        rows = self.cur.execute("SELECT * from SIGHTINGS Where SIGHTINGS.NAME =? ORDER BY SIGHTINGS.sighted DESC LIMIT 10",(name,)).fetchall()
        return rows

    def create(self,params):
        query = f'insert into SIGHTINGS ' \
                f'(Name, Person, Location, Sighted) ' \
                f'values ("{params.get("Name")}","{params.get("Person")}",' \
                f'"{params.get("Location")}","{params.get("Sighted")}")'
        self.conn.execute(query)
        return


class Flowers:
    def __init__(self):
        self.conn = sqlite3.connect('flowers2019.db')
        self.cur = self.conn.cursor()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def getNames(self):
        rows = self.cur.execute("SELECT comname From flowers").fetchall()
        return rows

    def update(self, params):
        query = f'UPDATE flowers ' \
                f'SET genus = "{params.get("Genus")}",species = "{params.get("Species")}", ' \
                f'comname = "{params.get("CommonName")}" ' \
                f'WHERE comname = "{params.get("Flowers")}";'
        self.cur.execute(query)
        return

    def select(self):
       return self.cur.execute('SELECT * FROM FLOWERS').fetchall()

    


