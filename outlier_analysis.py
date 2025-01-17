# There is a tradeoff between using numpy and sqlite3 for different things
import sqlite3
import numpy as np
import pandas as pd

# Connect to database
conn = sqlite3.connect("predictit.db")
c = conn.cursor()

# Load data for analysis
data = pd.read_sql("select * from contracts", con=conn)
print(data.head())

# Group data by contract id
contracts = data.groupby(["market_name", "contract_name"])

# Determine which contract has most volatility
def top_volatility(data):
    std_buy_yes = contracts['buy_yes'].std()
    std_sell_yes = contracts['sell_yes'].std()
    std_buy_no = contracts['buy_no'].std()
    std_sell_no = contracts['sell_no'].std()

    print("Most volatile buy yes:")
    print(std_buy_yes.sort_values(ascending=False).head())

    print("Most volatile sell yes:")
    print(std_sell_yes.sort_values(ascending=False).head())

    print("Most volatile buy no:") 
    print(std_buy_no.sort_values(ascending=False).head())

    print("Most volatile sell no:")
    print(std_sell_no.sort_values(ascending=False).head())

# Execute all analyses
top_volatility(data)

# Close database connection without saving changes
conn.close()