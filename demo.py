import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=database')


# Open a cursor to perform database operations
cursor = connection.cursor()

# drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")
# populate the vlaues to the cursor

# cursor.execute('INSERT INTO todos (id, description) VALUES (1, true);')

# Exercise 2 now use %s and %(named_var)s to fill the values dynamically

data = {
    'id': 2,
    'description': False
}

SQL = 'INSERT INTO todos (id, description) VALUES (%(id)s, %(description)s);'

cursor.execute('INSERT INTO todos (id, description) VALUES '
               '(%s, %s);',(1, True))

cursor.execute(SQL, data)

cursor.execute('INSERT INTO todos (id, description) VALUES '
               '(%s, %s);', (3, True))

# Read the data inserted on the database

cursor.execute('SELECT * from todos;')

# result = cursor.fetchall()
# Use fetchmany instead of fetchall
result = cursor.fetchmany(2)
print('fetchmany', result)

# use fetchone to understand the difference
result2 = cursor.fetchone()
print('fetchone', result2)

# Execute a Select query again so that a new fetch pipline is ready
cursor.execute('SELECT * from todos;')
result3 = cursor.fetchone()
print('fetchone', result3)

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()

