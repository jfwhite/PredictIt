# There is a tradeoff between using numpy and sqlite3 for different things
import sqlite3
import numpy as np

# Connect to database
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Prepare table by deleting rows with missing data
c.execute("DELETE FROM coursedata WHERE dim1 = -1")
c.execute("DELETE FROM coursedata WHERE dim2 = -1")
c.execute("DELETE FROM coursedata WHERE dim3 = -1")

# Figure out which dimension to present to the user
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
    # return dimension with greatest standardized range
    return sorted(results)[-1][1] 

# Execute one iteration of our algorithm
def step():
    dim = sorted(which_col())

# Take a look at current state of coursedata table
#c.execute("SELECT * FROM coursedata")
#for row in c.fetchall():
#    print "\t\t".join([str(col) for col in row])

# Close database connection without saving changes
conn.close()
