import sqlite3

CREATE_GROUPS = """
   CREATE TABLE IF NOT EXISTS groups (
   name TEXT PRIMARY KEY
   )
   """
CREATE_PEOPLE = """
   CREATE TABLE IF NOT EXISTS people (
   name TEXT PRIMARY KEY,
   p_group TEXT,
   amount_paid REAL,
   FOREIGN KEY (p_group) REFERENCES groups (name)
   )
   """
CREATE_MENU_ITEMS = """
   CREATE TABLE IF NOT EXISTS menu_items (
   name TEXT,
   mi_group TEXT, 
   price REAL, 
   qty INTEGER,
   PRIMARY KEY (name, mi_group),
   FOREIGN KEY (mi_group) REFERENCES groups (name)
   )
   """

def main():

   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute(CREATE_GROUPS)
   c.execute(CREATE_PEOPLE)
   c.execute(CREATE_MENU_ITEMS)

   # Turn on foreign keys
   c.execute("PRAGMA foreign_keys = ON")
   db.commit()
   try:
      c.execute("INSERT INTO groups (name) VALUES ('A')")
      c.execute("INSERT INTO groups (name) VALUES ('B')")
      db.commit()
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sienna', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Emily', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sandeep', 'A', 0)")
      db.commit()
      # Make sure you commit before this line, because this line raises an exception so nothing after it will occur.
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Hayden', 'C', 0)")

      db.commit()
   except sqlite3.IntegrityError as e:
      print(e)
   c.close()
   db.close()

if __name__ == "__main__":
   main()