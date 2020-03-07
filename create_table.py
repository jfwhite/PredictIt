# Create connection to database
import sqlite3
conn = sqlite3.connect("predictit.db")
c = conn.cursor()

# Create new coursedata table
statement = "create table if not exists coursedata ({}, {}, {}, {}, {})"
statement = statement.format(
	"course_id text primary key",
	"course_title text", 
	"course_level int", 
	"course_category int", # How STEMmy the course is
	"course_enrollment int", 
)
c.execute(statement)

# Close connection to database after saving changes
conn.commit()
conn.close()
