import sqlite3

#the below line to store the database permantently in the memory

#conn = sqlite3.connect(':memory:')

#creating a database

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# create a Table
#doc string 6 quotation marks

#c.execute("""CREATE TABLE customers123(
#          first_name text,
#          last_name text,
#          email text,
#          phone_number integer
#         )""")

c.execute("INSERT INTO customers123 VALUES('cole', 'walter', 'cole@walter.com', 7635489450)") 
c.execute("INSERT INTO customers123 VALUES ('conrad', 'fisher', 'conrad@fisher.com', 5467398702)")
c.execute("INSERT INTO customers123 VALUES('belly', 'conklin', 'belly@conklin.com', 3452117559)") 

c.execute("SELECT * FROM customers123")
print(c.fetchall())
conn.commit()