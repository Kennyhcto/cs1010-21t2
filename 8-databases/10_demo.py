import sqlite3

CREATE_GROUPS_TABLE = "CREATE TABLE IF NOT EXISTS groups (name TEXT PRIMARY KEY)"
CREATE_PEOPLE_TABLE = """
        CREATE TABLE IF NOT EXISTS people (
            name TEXT PRIMARY KEY,
            p_group TEXT,
            amount_paid REAL,
            FOREIGN KEY (p_group) REFERENCES groups (name)
            )
            """
CREATE_MENU_ITEMS_TABLE = """
        CREATE TABLE IF NOT EXISTS menu_items (
            name TEXT,
            mi_group TEXT,
            price REAL,
            qty INTEGER,
            PRIMARY KEY (name, mi_group),
            FOREIGN KEY (mi_group) REFERENCES groups (name)
        )
    """

def set_up_database():
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Turn on foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")
    db.commit()

    # Create the groups table
    # Making name column a PRIMARY KEY so duplicate names will not be allowed
    cursor.execute(CREATE_GROUPS_TABLE)
    cursor.execute(CREATE_PEOPLE_TABLE)
    cursor.execute(CREATE_MENU_ITEMS_TABLE)
    db.commit()
    cursor.close()
    db.close()

def insert_sample_data():
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()
    
    # Insert some groups into the groups table
    try:
        cursor.execute("INSERT INTO groups VALUES ('A')")
        cursor.execute("INSERT INTO groups VALUES ('B')")
        cursor.execute("INSERT INTO groups VALUES ('C')")
        cursor.execute("INSERT INTO people VALUES ('Sienna', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Vivian', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Gaby', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Hayden', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Sandeep', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Emily', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Nick', 'A', 0)")
        cursor.execute("INSERT INTO people VALUES ('Bart', 'B', 0)")
        cursor.execute("INSERT INTO people VALUES ('Luke', 'B', 0)")
        cursor.execute("INSERT INTO people VALUES ('Cliff', 'C', 0)")
        cursor.execute("INSERT INTO people VALUES ('Sim', 'C', 0)")
        cursor.execute("INSERT INTO menu_items VALUES ('Formaggi', 'A', 26, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Gamberi', 'A', 26, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Bufala', 'C', 26, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Melanzane', 'B', 26, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Vegan Mozarella', 'B', 5, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Lamb Fettaccine', 'A', 26, 2)")
        cursor.execute("INSERT INTO menu_items VALUES ('Risotto', 'A', 26, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('L.L.Bitters', 'A', 4, 1)")
        cursor.execute("INSERT INTO menu_items VALUES ('Coke', 'C', 4, 1)")

    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        db.commit()

    cursor.close()
    db.close()

'''
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    cursor.close()
    db.close()
'''

'''
Groups Dictionary Structure

groups = {
    'A' : {},
    'B' : {},
    'C' : {}
}

groups = {
    'A' : {'size':5, 'total_spent':160.25},
    'B' : {'size':2, 'total_spent':20.17},
    'C' : {'size':2, 'total_spent':19.99}
}

People Dictionary Structure

people = {
    'Sienna' : {},
    'Vivian' : {},
    'Bart' : {}
}

people = {
    'Sienna' : {'group':'A', 'amount_paid':0},
    'Vivian' : {'group':'A', 'amount_paid':0},
    'Bart' : {'group':'B', 'amount_paid:0}
}

Menu Items Dictionary Structure

menu_items = [
    {'name':'Pizza', 'group':'A', 'price':26.5, 'qty':2}
]
'''

def get_all_groups():
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create empty dictionary for our groups
    groups = {}

    # Get all the groups from the database
    cursor.execute("SELECT * FROM groups")
    rows = cursor.fetchall()

    # Go through the results, entering them
    # into our dictionary
    for row in rows:
        name = row[0]
        groups[name] = {}

    cursor.close()
    db.close()

    return groups

def get_all_people():
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create empty dictionary for our people
    people = {}

    # Get all the people from the database
    cursor.execute("SELECT * FROM people")
    rows = cursor.fetchall()

    # Go through the results, entering them
    # into our dictionary
    for row in rows:
        #print(row)
        name = row[0]
        group = row[1]
        people[name] = {}
        people[name]['group'] = group
        people[name]['amount_paid'] = 0

    cursor.close()
    db.close()

    return people

def get_all_menu_items():
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create empty list for our menu items
    menu_items = []

    # Get all the menu items from the database
    cursor.execute("SELECT * FROM menu_items")
    rows = cursor.fetchall()

    # Go through the results, entering them
    # into our dictionary
    for row in rows:
        #print(row)
        menu_items.append({
            'name':row[0],
            'group':row[1],
            'price':row[2],
            'qty':row[3]
        })

    cursor.close()
    db.close()

    return menu_items

def get_size_of_group(group_name):
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Get all the people from the database
    cursor.execute(f"SELECT * FROM people WHERE p_group='{group_name}'")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return len(rows)

def calculate_groups_sizes(groups):
    for group in groups:
        groups[group]['size'] = get_size_of_group(group)

def get_all_menu_items_for_group(group_name):
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create empty list for our menu items
    menu_items = []

    # Get all the menu items from the database
    cursor.execute(f"SELECT * FROM menu_items WHERE mi_group='{group_name}'")
    rows = cursor.fetchall()

    # Go through the results, entering them
    # into our dictionary
    for row in rows:
        #print(row)
        menu_items.append({
            'name':row[0],
            'group':row[1],
            'price':row[2],
            'qty':row[3]
        })

    cursor.close()
    db.close()

    return menu_items

def get_total_spent_for_group(group_name):

    # Get all the items for that group
    items_for_group = get_all_menu_items_for_group(group_name)

    total_spent = 0

    # Add up the total spent
    for item in items_for_group:
        total_spent += item['price'] * item['qty']

    return total_spent

def calculate_groups_total_spent(groups):
    for group in groups:
        groups[group]['total_spent'] = get_total_spent_for_group(group)

def calculate_people_owing(groups, people):
    calculate_groups_sizes(groups)
    calculate_groups_total_spent(groups)
    # For each person
    for person in people:
        # Get their group
        group_name = people[person]['group']
        group_data = groups[group_name]
        # Get the amount owed per person for their group
        owed_for_their_group = group_data['total_spent']/group_data['size']
        # Subtract what they've already paid
        # Set that as what they owe
        people[person]['amount_owing'] = owed_for_their_group - people[person]['amount_paid']

def add_payment(people, person_name, payment_amount):
    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Update dictionary
    people[person_name]['amount_paid'] += payment_amount

    new_amount_paid = people[person_name]['amount_paid']

    # Update database
    cursor.execute(f"""
                UPDATE people
                SET amount_paid = {new_amount_paid}
                WHERE name ='{person_name}'""")

    cursor.close()
    db.close()


def main():

    #set_up_database()
    #insert_sample_data()
    groups = get_all_groups()
    people = get_all_people()
    menu_items = get_all_menu_items()
    #print(people)


    calculate_people_owing(groups, people)
    #print(groups)
    #print(people)

    add_payment(people, 'Sienna', 5)
    add_payment(people, 'Sim', 2.45)

    calculate_people_owing(groups, people)
    print(groups)
    print(people)


    


if __name__ == "__main__":
    main()