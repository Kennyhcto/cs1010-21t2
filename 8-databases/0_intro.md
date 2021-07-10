# Databases Introduction

A database is an organized collection of data stored and accessed electronically from a computer system.

## Why Use Databases?

* Persistence (so we don't lose our data when the application closes) (just like saving in a file).
* It allows us to access and summarize data more quickly/simply/easily.

Side Note: Databases are a great skill to have outside of what's generally considered 'programming'. There are database applications which use SQL but do not require other programming skills. In these cases, it is useful, in life and workplace, to understand and be able to use/look up how to do things.

## SQL

SQL (Structured Query Language) is a standard language for accessing and manipulating databases.

Note: There are different versions, but major (most commonly used) commands are supported in similar ways.

We will use sqlite3 in this course as it comes packaged with Python and does not require its own server running. Most of the skills you learn, can be adapted to any other SQL database.

## Terminology

* table: a collection of related data entries
* field: a column of a table
* record (or entry): a row of a table

## Notes

* A database consists of one or more tables.
* Much like a variable, each field (or column) has a name, and a type.
* You can think of a database table as a list (lots of rows) of dictionaries (each column is a part of the dictionary) in Python.

## Approximate Roadmap

Each demo builds on the one before.
* Sometimes we will improve an approach, so remove old code and replace it with better code.
* Sometimes we will only add new code to add functionality to the program.
* Demo 10 contains the best of our code, and all the functionality from earlier demonstrations.

1. Creating tables. (1-2)
2. Inserting data into the tables. (3,6,8)
3. Primary keys. (4-5)
4. Foreign keys. (7)
5. Getting data from tables. (10)

## Types of Demos

* Demos - Python code showing how to use your database from a Python program.
* Direct to the database - Accessing the database directly to:
   * check our Python code is working
   * learn SQL
   * build familiarity with databases

## Demo Introduction

* Splitting the bill: Look over spreadsheet version

## Demos

* Aside: Draw a diagram for `groups` table.
* 1 - Create a table of `groups`. Each group should have a unique name.
   * What happens if we try to create a table which already exists?
   * How can we fix this?
* 2 - Create a table with IF NOT EXISTS to avoid the problem in `demo_1.py`.

## Direct to the database: Inspecting

Command-line commands (for use in the terminal):
* Connect to the database: `sqlite3 split_the_bill.db`
* Get table names:
```sql
select name from sqlite_master where type="table";
```
* Get table schema (structure): `.schema groups`
* ctl-D to exit command-line connection
* Up-Arrow scrolls through previous commands

## Direct to the database: SELECT and INSERT INTO

* \* means 'all'
* -- creates a comment

```sql
-- Get all rows and columns from a table
SELECT * from table_name;

-- Get only the listed fields (columns) from a table
SELECT field_1_name, field_2_name, ... from table_name;

-- Get all fields (columns) from a table, where the condition is met
SELECT * from table_name WHERE field_name = 'value';

-- Insert the values into the table (must list all the fields, in the correct order)
INSERT INTO table_name VALUES (field_1_value, field_2_value, ...);

-- Insert the values into the table where you only have some fields to put in
INSERT INTO table_name (field_1_name, field_2_name, ...) VALUES (field_1_value, field_2_value, ...);
```

## Demos

* 3 - Insert some groups into the table.
   * What happens if we try and insert a group with a name which is already used?
   * How can we address this? (We wanted group names to be unique.)

## Primary Keys

* Used to make each row uniquely identifiable
* Like a row number in a spreadsheet
* Must be unique
* Can be automatically generated (for more information, look [here](https://www.tutorialspoint.com/sqlite/sqlite_using_autoincrement.htm))
* Can be made up of more than one field
* To make a field a primary key, add `PRIMARY KEY` to the end of its declaration.
* To make a composite primary key, add a line to the table creation `PRIMARY KEY (field_1, field_2...)` at the end of the table creation.

## Demos

* 4 - Delete your existing database. Change demo 3, but make it so that the `name` field of the `groups` table is a primary key.
   * What happens *now* when you try to insert the same value multiple times?
* 5 - Change demo 4 so that it elegantly handles the `sqlite3.IntegrityError` exception that was raised if someone tries to insert the same group multiple times.
* Aside: Draw a diagram for People table and Menu_Items table.
   * people: name as primary key, p_group, amount they've paid (NOTE: we can't use `group` as a column name because it's a keyword in SQL.)
   * menu_items: name and mi_group create the primary key, price, quantity
* 6 - Create a full set of tables for Splitting the Bill. Insert some people into the `people` table.
   * What happens if you give someone a group name which doesn't exist?
   * Can we enforce assigning people only to groups which currently exist?

## Foreign Keys

* Used when a field in one table references a field in another table.
* Make sure your database is enforcing foreign keys:
```sql
c.execute("PRAGMA foreign_keys = ON")
db.commit()
```
* Make a field a foreign key:
```sql
FOREIGN KEY (field_name) REFERENCES table_name (other_field_name)
```

## Demos

* 7 - Update `demo_6.py` so that only groups already in the `groups` table can be used in the `people` and `menu_items` tables.
* 8 - Populate the tables with some sample data.
* 9 - Refactor your code (if you haven't already) from `demo_8.py` to make it ready to be used in a bigger application.

## Accessing Information and Using It

Looking back at week 1, what information would be useful to get from our database?

* The size of each group.
* The amount spent by each group.

Keeping your application in its improved layout, implement the functionality listed below.

* 10 - Write the following functions:
   * Get all the groups (into a dictionary). `get_all_groups()`
   * Get all the people (into a dictionary). `get_all_people()`
   * Get all the menu items (into a dictionary). `get_all_menu_items()`

   * Update the groups dictionary to include the size of each group. `calculate_groups_sizes(groups)`
      * Get all the people for a given group. `get_all_people_for_group(group_name)`
      * Get the size of a given group. `get_size_of_group(group_name)`
   * Update the groups dictionary to include the total spent for each group. `calculate_groups_total_spent(groups)`
      * Get all the menu items for a given group. `get_all_menu_items_for_group(group_name)`
      * Get the total spent for a given group. `get_total_spent_for_group(group_name)`
   * Fill out the people list with the amount they owe. (Initial owing, minus what they have already paid.)`calculate_people_owing(groups, people)`
   * Update table and dictionary with amount that someone has paid. `add_payment(person_name, payment_amount)`



## Another example:
* Tutorials: course_code, code, tutor
* Courses: course_code, title
* Students: zid, fname, lname
* Enrollments: course_code, tute_code, zid


## Feedback

Lecture: 8 - Databases

![](https://i.imgur.com/5FKvgmw.png)


[Link to feedback form](https://forms.gle/NdAhw7ZMJ2eBEydd7)
