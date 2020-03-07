import sqlite3
import requests
import sys

# Connect to database
conn = sqlite3.connect("predictit.db")
c = conn.cursor()

# Delete existing rows if desired
if len(sys.argv) > 2:
    if sys.argv[2] == "overwrite":
        c.execute("delete from contracts")

# Get data from API
response = requests.get("https://www.predictit.org/api/marketdata/all")
data = response.json()

# Template for insertion
template = "insert into contracts values "
template += "({}, '{}', '{}', {}, '{}', '{}', {}, {}, {}, {}, {}, {})"

# Insert data into contracts table
for market in data.get("markets", []):    
    for contract in market.get("contracts", []):
        statement = template.format(
            market['id'],
            market['shortName'].replace("'", ""),
            market['timeStamp'].replace("T", " ").split(".")[0],
            contract["id"],
            contract["shortName"].replace("'", ""),
            contract["dateEnd"].replace("T", " ").split(".")[0],
            round(100*contract["bestBuyYesCost"]) if contract["bestBuyYesCost"] else 'null',
            round(100*contract["bestBuyNoCost"]) if contract["bestBuyNoCost"] else 'null',
            round(100*contract["bestSellYesCost"]) if contract["bestSellYesCost"] else 'null',
            round(100*contract["bestSellNoCost"]) if contract["bestSellNoCost"] else 'null',
            round(100*contract["lastTradePrice"]) if contract["lastTradePrice"] else 'null',
            round(100*contract["lastClosePrice"]) if contract["lastClosePrice"] else 'null',
        )

        print(statement)
        c.execute(statement)

# Close database connection
conn.commit()
conn.close()
