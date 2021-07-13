import sqlite3


def main():
    db = sqlite3.connect('8-databases/split_the_bill.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE groups (name TEXT)")
    db.commit()
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()