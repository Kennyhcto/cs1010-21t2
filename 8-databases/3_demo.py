import sqlite3


def main():

    # Connect to the database
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()

    # Create the groups table
    cursor.execute("CREATE TABLE IF NOT EXISTS groups (name TEXT)")
    db.commit()

    # Insert some groups into the groups table
    cursor.execute("INSERT INTO groups VALUES ('A')")
    cursor.execute("INSERT INTO groups VALUES ('A')")
    cursor.execute("INSERT INTO groups VALUES ('C')")
    db.commit()

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()