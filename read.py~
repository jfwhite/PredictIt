import sqlite3
import numpy as np

conn = sqlite3.connect("courses.db")
c = conn.cursor()

c.execute("DELETE FROM coursedata WHERE dim1 = -1")
c.execute("DELETE FROM coursedata WHERE dim2 = -1")
c.execute("DELETE FROM coursedata WHERE dim3 = -1")

def which_col():
    c.execute("SELECT dim1 FROM coursedata")
    d1 = [float(row[0]) for row in c.fetchall()]
    r1 = (max(d1) - min(d1))/np.std(d1)

    c.execute("SELECT dim2 FROM coursedata")
    d2 = [float(row[0]) for row in c.fetchall()]
    r2 = (max(d2) - min(d2))/np.std(d2) # watch out for dividing by zero

    c.execute("SELECT dim3 FROM coursedata")
    d3 = [float(row[0]) for row in c.fetchall()]
    r3 = (max(d3) - min(d3))/np.std(d3)

    results = [ (r1, d1), (r2, d2), (r3, d3) ]
    return sorted(results)[-1][1]

def step():
    dim = sorted(which_col())

#c.execute("SELECT * FROM coursedata")
#for row in c.fetchall():
#    print "\t\t".join([str(col) for col in row])

# how much do I use the database for?
conn.close()
