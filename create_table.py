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
	"market_id integer",
	"market_name text",
	"timestamp text",
	"contract_id integer",
	"contract_name text",
	"contract_end text",
	"buy_yes integer", 
	"buy_no integer", 
	"sell_yes integer",
	"sell_no integer",
	"last_trade integer",
	"last_close integer"
)
c.execute(statement)

# Close connection to database after saving changes
conn.commit()
conn.close()
