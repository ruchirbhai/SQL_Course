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
todo_id = '1'
todo_status = 'true'
cursor.execute('INSERT INTO todos (id, description) VALUES '
               '(%s, %s);',(1, True))

cursor.execute('INSERT INTO todos (id, description) VALUES '
               '(%(todo_id)s, %(todo_status)s);', {
                'todo_id': 2,
                'todo_status': False})

# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()

