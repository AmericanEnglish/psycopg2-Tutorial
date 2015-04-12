# Now you've setup the initial stuff and gotten all the psycopg2 ready

import psycopg2
con = psycopg2.connect(host='localhost', database='cs350', user='student', password='student')
cur = con.cursor()

# Let's say you've just setup a table of names and their wallet change:

cur.execute("""
    CREATE TABLE wallet_change
    (
        name VARCHAR(20),
        change MONEY
        PRIMARY KEY (name)
    );""")

con.commit()

# Then some data 

cur.execute("""INSERT INTO wallet_change VALUES
    (stacy, 10.00),
    (luis, 2.50),
    (steven, 0.00),
    (mary, 5.00),
    (jamal, 12.99);""")

con.commit()

# UGH WHAT DID MARY HAVE? Well that's a simple select statement:
cur.execute("""SELECT name, change 
    FROM wallet_change 
    WHERE name = 'mary'""")


# Now to fetch the data:
data = cur.fetchall()

# Now the interesting thing is that data is actually a list of tuples!
print("data is {}".format(type(data)))
print("the DATA in data is {}".format(type(data[0])))

# So to access it we can simply just use a loop or in some cases just an easy index:
print("Name: {}\nChange: {}".format(data[0][0], data[0][1]))

# Although these are some easy examples but what if i dont want to type that sql statement
# everytime, i just want an easy function. NO PROBLEM!
def display_monies(name, cur):
    cur.execute("""SELECT change FROM wallet_change WHERE name = %s""", [name])
    data = cur.fetchall()
    return data[0]

# See when you need to insert data into an SQL statement you must NEVER
# NEVER
# EVER
# EVER----------------------------------~
# USE STRING METHODS.
# This results in SQL Injection. -> Google it if that doesn't make sense. Just know == bad
# You can insert data into these strings saftely with the following methods ONLY

cur.execute("""SELECT * FROM wallet_change WHERE name = %s""", (name,))

# OR

cur.execute("""SELECT * FROM wallet_change WHERE name = %s""", [name])

# Never use any other form of %, not %d, %f , none of it.

# Note that psycopg2 can convert python datatypes super well in a lot of cases for examples
# please see their documentation:
print('http://initd.org/psycopg/docs/usage.html')

# This will be expanded as i feel is needed