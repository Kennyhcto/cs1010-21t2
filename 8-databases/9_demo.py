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

def create_tables():
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute(CREATE_GROUPS)
   c.execute(CREATE_PEOPLE)
   c.execute(CREATE_MENU_ITEMS)

   # Turn on foreign keys
   c.execute("PRAGMA foreign_keys = ON")
   db.commit()
   c.close()
   db.close()

def insert_sample_data():
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   try:
      c.execute("INSERT INTO groups (name) VALUES ('A')")
      c.execute("INSERT INTO groups (name) VALUES ('B')")
      c.execute("INSERT INTO groups (name) VALUES ('C')")
      db.commit()
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sienna', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Emily', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sandeep', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Vivian', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Nick', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Bart', 'B', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Luke', 'B', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Gaby', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Cliff', 'C', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Hayden', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Sim', 'C', 0)")

      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Tartufata', 'A', 24, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Formaggi', 'A', 26, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Bufala', 'A', 24, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Gamberi', 'A', 29, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Melanzane', 'A', 24, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Vegan Mozarella', 'B', 5, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Lamb Fettaccine', 'A', 26, 2)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Risotto', 'A', 27, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('L.L.Bitters', 'A', 4, 1)")
      c.execute("INSERT INTO menu_items (name, mi_group, price, qty) VALUES ('Coke', 'C', 4, 1)")
      db.commit()
   except sqlite3.IntegrityError as e:
      print(e)
   c.close()
   db.close()

def main():
   create_tables()
   insert_sample_data()

if __name__ == "__main__":
   main()