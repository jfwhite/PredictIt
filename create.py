# Create connection to database
import sqlite3
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Drop old coursedata table
c.execute("DROP TABLE IF EXISTS COURSEDATA")

# Create new coursedata table
statement = "CREATE TABLE IF NOT EXISTS COURSEDATA (cids text PRIMARY KEY, "
statement = statement + "{c1}, {c2}, {c3}, {c4}, {c5})"
c1 = "dim1 int" # The course level
c2 = "dim2 int" # The STEM-ness
c3 = "dim3 int" # The enrollment
c4 = "name text"# the name
c5 = "rating text" # the rating

c.execute(statement.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5))

# Close connection to database after saving changes
conn.commit()
conn.close()
