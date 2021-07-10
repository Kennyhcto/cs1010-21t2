'''
   * people: name as primary key, p_group, amount they've paid
   * menu_items: name and group create the primary key, price, quantity
   '''


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
   amount_paid REAL
   )
   """
CREATE_MENU_ITEMS = """
   CREATE TABLE IF NOT EXISTS menu_items (
   name TEXT,
   mi_group TEXT, 
   price REAL, 
   qty INTEGER,
   PRIMARY KEY (name, mi_group)
   )
   """

def main():

   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute(CREATE_GROUPS)
   c.execute(CREATE_PEOPLE)
   c.execute(CREATE_MENU_ITEMS)
   db.commit()
   try:
      c.execute("INSERT INTO groups (name) VALUES ('A')")
      c.execute("INSERT INTO groups (name) VALUES ('B')")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sienna', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Emily', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sandeep', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Hayden', 'C', 0)")

      db.commit() # this is essential, and it executes all the "execute" statements we've done since the last commit.
   except sqlite3.IntegrityError:
      print("Didn't insert groups because they're already there.")
   c.close()
   db.close()

if __name__ == "__main__":
   main()