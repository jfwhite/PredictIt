import sqlite3
import requests

# Connect to database
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Get data from API
response = requests.get("https://www.predictit.org/api/marketdata/all")
data = response.json()

# Template for insertion
template = "insert into contracts values "
template += "({}, '{}', {}, {}, '{}', {}, {}, {}, {}, {}, {}, {})"

# Insert data into contracts table
for market in data.get("markets", []):    
    for contract in market.get("contracts", []):
        statement = template.format(
            market['id'],
            market['shortName'],
            market['timeStamp'].replace("T", "").split(".")[0],
            contract["id"],
            contract["shortName"],
            contract["dateEnd"],
            contract["bestBuyYesCost"],
            contract["bestBuyNoCost"],
            contract["bestSellYesCost"],
            contract["bestSellNoCost"],
            contract["lastTradePrice"],
            contract["lastClosePrice"],
        )

        c.execute(statement)

# Close database connection
conn.commit()
conn.close()
