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

# Transfer data from database to NumPy
c.execute("SELECT * FROM coursedata")
sqldata = c.fetchall()
dtype = [('id', 'S10'), ('dim1', int), ('dim2', int), ('dim3', int)]
data = np.array(sqldata, dtype=dtype)

# Figure out which dimension to present to the user
def which_col(data):
    results = []

    d1 = [float(val) for val in data["dim1"]]
    if max(d1) != min(d1):
        r1 = (max(d1) - min(d1))/np.std(d1)
        results.append((r1, "dim1"))

    d2 = [float(val) for val in data["dim2"]]
    if max(d2) != min(d2):
        r2 = (max(d2) - min(d2))/np.std(d2) 
        results.append((r2, "dim2"))

    d3 = [float(val) for val in data["dim3"]]
    if max(d3) != min(d3):
        r3 = (max(d3) - min(d3))/np.std(d3)
        results.append((r3, "dim3"))

    # return dimension with greatest standardized range
    return max(results)[1] 

def print_options(low, med, high):
    print "Here are three example courses:"
    print "ID: " + low[0] 
    print "ID: " + med[0]
    print "ID: " + high[0]

def parse(selection):
    if selection in ["1", "2", "3"]:
        return int(selection)
    else:
        return parse(raw_input("Please enter 1, 2, or 3.\n"))

def top_courses(newdata):
    return newdata[0][0]

# Execute one iteration of our algorithm
def step(data):
    col = which_col(data)
    sor = np.sort(data, kind='mergesort', order=col)
    print_options(sor[0], sor[len(sor)/2], sor[-1])
    print "Based on the dimension of " + col + "..."
    selection = parse(raw_input("Do you prefer course 1, 2, or 3?\n"))    
    return sor[(selection-1)*len(sor)/3: selection*len(sor)/3]

for i in range(10):
    print "__________________________________________"
    newdata = step(data)
    print "Your top courses are: " + top_courses(newdata)
    print "There are " + str(len(newdata)) + " courses remaining"
    if len(newdata) < 10:
        print "Stopping execution because there are too few courses"
        break
    data = newdata

# Close database connection without saving changes
conn.close()

# Try numpy, pandas, SQLite, SQLAlchemy and see which is faster
# or just zipping
