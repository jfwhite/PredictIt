import sqlite3

conn = sqlite3.connect("courses.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS COURSEDATA")

statement = "CREATE TABLE IF NOT EXISTS COURSEDATA "
statement = statement + "(id text PRIMARY KEY, {c1}, {c2}, {c3})"

col1 = "dim1 text"
col2 = "dim2 text"
col3 = "dim3 text"

c.execute(statement.format(c1 = col1, c2 = col2, c3 = col3))

conn.commit()
conn.close()
