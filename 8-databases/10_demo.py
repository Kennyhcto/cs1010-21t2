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
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Hayden', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Bart', 'B', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Luke', 'B', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Gaby', 'A', 0)")
      c.execute("INSERT INTO people (name, p_group, amount_paid) VALUES ('Cliff', 'C', 0)")
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

'''
   * Get all the groups.
   * Get all the people.
   * Get all the menu items.
   * Get all the people for a given group.
      * Get the size of a given group.
   * Get all the menu items for a given group.
      * Get the total spent for a given group.
'''

def get_all_groups():
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("SELECT * from groups")
   rows = c.fetchall()
   groups = {}
   for row in rows:
      #groups.append({'name':row[0]})
      groups[row[0]] = {}
   c.close()
   db.close()
   return groups

def get_all_people():
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("SELECT * from people")
   rows = c.fetchall()
   people = {}
   for row in rows:
      #people.append({'name':row[0], 'group':row[1], 'amount_paid':row[2]})
      people[row[0]] = {'group':row[1], 'amount_paid':row[2]}
   c.close()
   db.close()
   return people

def get_all_menu_items():
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("SELECT * from menu_items")
   rows = c.fetchall()
   items = {}
   for row in rows:
      #items.append({'name':row[0], 'group':row[1], 'price':row[2], 'qty':row[3]})
      items[(row[0], row[1])] = {'price':row[2], 'qty':row[3]}
   c.close()
   db.close()
   return items

def get_all_people_for_group(group_name):
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute(f"SELECT * from people WHERE p_group = '{group_name}'")
   rows = c.fetchall()
   people = {}
   for row in rows:
      #people.append({'name':row[0], 'group':row[1], 'amount_paid':row[2]})
      people[row[0]] = {'group':row[1], 'amount_paid':row[2]}
   c.close()
   db.close()
   return people

def get_size_of_group(group_name):
   return len(get_all_people_for_group(group_name))

def get_all_menu_items_for_group(group_name):
   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute(f"SELECT * from menu_items WHERE mi_group = '{group_name}'")
   rows = c.fetchall()
   items = []
   for row in rows:
      items.append({'name':row[0], 'group':row[1], 'price':row[2], 'qty':row[3]})
   c.close()
   db.close()
   return items

def get_total_spent_in_group(group_name):
   sum = 0
   for item in get_all_menu_items_for_group(group_name):
      sum += item['price'] * item['qty']
   return sum


def calculate_groups_sizes(groups):
   for group in groups:
      groups[group]['size'] = get_size_of_group(group)

def calculate_groups_total_spent(groups):
   for group in groups:
      groups[group]['total_spent'] = get_total_spent_in_group(group)

'''


Fill out the people list with the amount they owe. (Initial owing, minus what they have already paid.)calculate_people_owing(groups, people)

Update table and dictionary with amount that someone has paid. add_payment(person_name, payment_amount)
'''

def main():
   #create_tables()
   #insert_sample_data()
   groups = get_all_groups()
   people = get_all_people()
   items = get_all_menu_items()

   print(groups)
   print()
   print(people)
   print()
   #print(items)

   #print(get_all_people_in_group('C'))
   #calculate_owing(groups, people, items)

   calculate_groups_sizes(groups)
   calculate_groups_total_spent(groups)
   print(groups)

if __name__ == "__main__":
   main()