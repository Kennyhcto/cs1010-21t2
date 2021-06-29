"""
Comma Separated Values

Tabular (table-like) data can be stored in
Comma Separated Value (CSV) format.
"""

import csv


def get_sample_data_list():
    return [['T15A', 'Liz', 21],
            ['H12A', 'My Name Has A, Comma In It', 21],
            ['H15A', 'William', 21]]


def read_csv_as_list():
    
    # open file
    f = open('files/tutorials_list.csv', 'r')
    csv_reader = csv.reader(f)

    tutorials = []

    # read in lines from file to tutorials list
    for line in csv_reader:
        tutorials.append(line)

    # close the file
    f.close()

    # return the tutorials list
    return tutorials

def write_list_as_csv(tutorials):

    # open file for writing (saving)
    f = open('files/tutorials_list.csv', 'w')
    csv_writer = csv.writer(f)

    # write each element in tutorials list, into the file
    for tute in tutorials:
        csv_writer.writerow(tute)

    # close the file
    f.close()



if __name__ == "__main__":
    # read the file in
    data = read_csv_as_list()
    # make a change to the file
    data.append(['F09A','Kai',21])
    # write it out again
    write_list_as_csv(data)

