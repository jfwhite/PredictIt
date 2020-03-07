# There is a tradeoff between using numpy and sqlite3 for different things
import sqlite3
import numpy as np
import pandas as pd

# Connect to database
conn = sqlite3.connect("predictit.db")
c = conn.cursor()

# Get statistical summaries of data
statement = "select "
statement += "avg(buy_yes) as buy_yes_avg, "
statement += "avg(buy_no) as buy_no_avg, "
statement += "avg(sell_yes) as sell_yes_avg, "
statement += "avg(sell_no) as sell_no_avg, "
statement += "from contracts group by contract_id"
data = pd.read_sql(statement, con=conn)

# Determine which contract has most volatility
def top_volatility(data):
    # Do nothing

    print("Most volatile contracts:" 
    print(data.head())

# Execute all analyses
top_volatility(data)

# Close database connection without saving changes
conn.close()