# First import the extension:
import psycopg2

# Then use the login information, there are two ways to use it.

# Using a long string format
info = "host=localhost database=cs350 username=student password=student"
connection = psycopg2.connect(info)
# This closes the connection
connection.close()


# Using a standard variable style input
connection =  psycopg2.connection(host='localhost', database='cs350', user='student', password='password')

 # These two ways create connections to the database. Either way is approriate. 

 # Now you have basic cursor objects that allow you to interact with the database using SQL

 # Create a cursor:
 cur = connection.cursor()

 # Use the execute method. Also using triple quotes allows for extra newlines since SQL ignores this kind
 # whitespace
 cur.execute("""CREATE TABLE tablename
    (
        name CHAR(20),
        mynumber INTEGER(10),
    );""")

 # If you're only doing one statement the ; isn't needed but will be needed for several such as:
 cur.execute("""SELECT * FROM tablename;
    CREATE TABLE newtable
    (
        car_name VARCHAR(30),
        car_make VARCHAR(20),
        car_model VARCHAR(10),
    );""")

 # IF you execute a bad statement using the cursor the server you will be unable to execute
 # more statements until you 'rollback' the server

 cur.execute("""SELECT FROM tablename;""")
# Trying to do it again produces and error
try:
    cur.execute("""SELECT * FROM tablename;""")
except psycopg2.InternalError as error:
    print(error)


# To fix this you will need to do a rollback:
con.rollback()

# Likewise any data that has been changed must be committed to persist in the database:
con.commit()


