import sqlite3

def main():

   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("CREATE TABLE groups (name TEXT)")
   db.commit()
   c.close() # necessary only if you have more than one connection
   db.close()

if __name__ == "__main__":
   main()