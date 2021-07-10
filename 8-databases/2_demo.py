import sqlite3

def main():

   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("CREATE TABLE IF NOT EXISTS groups (name TEXT)")
   db.commit()
   c.close()
   db.close()

if __name__ == "__main__":
   main()