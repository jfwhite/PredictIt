# Create connection to database
import sqlite3
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Drop old coursedata table
c.execute("DROP TABLE IF EXISTS COURSEDATA")

# Create new coursedata table
statement = "CREATE TABLE IF NOT EXISTS COURSEDATA "
statement = statement + "(id text PRIMARY KEY, {c1}, {c2}, {c3})"
col1 = "dim1 int" # The course level
col2 = "dim2 int" # The STEM-ness
col3 = "dim3 int" # The enrollment
c.execute(statement.format(c1 = col1, c2 = col2, c3 = col3))

# Close connection to database after saving changes
conn.commit()
conn.close()
