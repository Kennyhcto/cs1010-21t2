import sqlite3


def main():

    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create the groups table
    # Making name column a PRIMARY KEY so duplicate names will not be allowed
    cursor.execute("CREATE TABLE IF NOT EXISTS groups (name TEXT PRIMARY KEY)")
    db.commit()

    # Insert some groups into the groups table
    try:
        cursor.execute("INSERT INTO groups VALUES ('A')")
        cursor.execute("INSERT INTO groups VALUES ('A')")
        cursor.execute("INSERT INTO groups VALUES ('C')")
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        db.commit()

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()