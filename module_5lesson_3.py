import sqlite3
print("import successful")

con = sqlite3.connect('sale.db')
print("connection successful")

cur = con.cursor()
print("cursor connection successful")

items = cur.fetchall()

for item in items:
    Item_ID, Item_name, price, quantity_lest_in_stock = item

#calculating the amount the business owner invested in the procurement of the items
cur.execute("select sum(price) from inventory1")
item = cur.fetchall()
print("The amount the business owner Invested in the procurement of the items: ",item)

#caalculating the average quantity of items in stock
cur.execute("select avg (quantity_lest_in_stock) from inventory1")
item = cur.fetchall()
print("The average quantity of items in stock: ",item)

#calculating the item with the least quantity in stock
cur.execute("select Item_name, min(quantity_lest_in_stock) from inventory1")
item = cur.fetchall()
print("The item with the least quantity in stock: ",item)


#calculating the item with the most quantity in stock
cur.execute("select Item_name, max(quantity_lest_in_stock) from inventory1")
item = cur.fetchall()
print("The item with the least quantity in stock: ",item)

#commit the database and table
con.commit()