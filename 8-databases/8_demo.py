import sqlite3


def main():

    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Turn on foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")
    db.commit()

    # Create the groups table
    # Making name column a PRIMARY KEY so duplicate names will not be allowed
    cursor.execute("CREATE TABLE IF NOT EXISTS groups (name TEXT PRIMARY KEY)")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            name TEXT PRIMARY KEY,
            p_group TEXT,
            amount_paid REAL,
            FOREIGN KEY (p_group) REFERENCES groups (name)
            )
            """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            name TEXT,
            mi_group TEXT,
            price REAL,
            qty INTEGER,
            PRIMARY KEY (name, mi_group),
            FOREIGN KEY (mi_group) REFERENCES groups (name)
        )
    """)
    db.commit()

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


if __name__ == "__main__":
    main()