# 2.4 - Serialisation and Persistence

Until now, when our application ends, all our data is lost.
If we want to save data, we need to write it into a file which continues
to exist after the program ends, and then be able to read it back into
the application when it starts up again.

Serialisation is the process of translating data structures into a format
such that they can be stored or transmitted.

Here we are going to look at 3 different ways of doing this:
1. Plain text file (`1_plain_text.py`)
2. CSV file
    a. storing lists (`2a_csv_list.py`)
    b. storing dictionaries (`2b_csv_dict.py`)
3. JSON file (`3_json.py`)


| File Type | Problem | Solution |
|---|---|---|
| Plain Text | <ul><li>How do we know when each piece of data starts and ends?</li><li>What if there is a newline in a piece of data?</li></ul> | CSV |
| CSV | What if there are:<ul><li>lists within lists?</li><li>lists within dictionaries?</li><li>dictionaries within lists?</li></ul> | JSON |
