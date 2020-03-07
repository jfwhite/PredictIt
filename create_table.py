import sqlite3
import sys

# Create connection to database
conn = sqlite3.connect("predictit.db")
c = conn.cursor()

# Drop contracts table if desired
if len(sys.argv) > 2:
	if sys.argv[2] == "overwrite":
		c.execute("drop table if exists contracts")

# Create new contracts table
statement = "create table if not exists contracts "
statement += "({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})"
statement = statement.format(
	"market_id int",
	"market_name text",
	"timestamp text",
	"contract_id int",
	"contract_name text",
	"contract_end text",
	"buy_yes int", 
	"buy_no int", 
	"sell_yes int",
	"sell_no int",
	"last_trade int",
	"last_close int"
)
c.execute(statement)

# Close connection to database after saving changes
conn.commit()
conn.close()
