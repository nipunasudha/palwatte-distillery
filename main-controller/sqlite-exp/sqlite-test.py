import sqlite3

conn = sqlite3.connect('company.db')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS employee (name, age)')
curs.execute("INSERT INTO employee VALUES ('Ali', 28)")
values = [('Brad', 54), ('Ross', 34), ('Muhammad', 28), ('Bilal', 44)]
curs.executemany('INSERT INTO employee VALUES(?,?)', values)
conn.commit()
conn.close()
