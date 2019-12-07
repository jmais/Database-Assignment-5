import sqlite3
con = sqlite3.connect('flowers2019.db')
cur = con.cursor()

t = ('California flannelbush',)
rows = cur.execute("SELECT * from SIGHTINGS Where SIGHTINGS.NAME =? ORDER BY SIGHTINGS.sighted DESC LIMIT 10",t)
for row in rows:
    print('name ' + str(row[0])+ 'person ' + str(row[1]) + 'location ' + str(row[2]) + 'sighted ' + str(row[3]))

con.close()