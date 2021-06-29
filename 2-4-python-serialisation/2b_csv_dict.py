"""
Comma Separated Values

Tabular (table-like) data can be stored in
Comma Separated Value (CSV) format.
"""

import csv


def get_sample_data_dict():
    return [{'tutorial':'T15A', 'tutor':'Liz', 'enrollments':21},
            {'tutorial':'H12A', 'tutor':'My Name Has A, Comma In It', 'enrollments':21},
            {'tutorial':'H15A', 'tutor':'William', 'enrollments':21}]



def read_csv_as_dict():
    # create empty list to read the file into
    tutorials = []

    # open the file
    f = open('files/tutorials_dict.csv', 'r')

    # create a dictionary reader
    csv_reader = csv.DictReader(f)

    # read in the file
    for row in csv_reader:
        tutorials.append(row)

    # close the file
    f.close()

    # return the information read in
    return tutorials


def write_dict_as_csv(tutorials):
    f = open('files/tutorials_dict.csv', 'w', newline='')
    csv_writer = csv.DictWriter(
        f, fieldnames=['tutorial', 'tutor', 'enrollments']
    )
    csv_writer.writeheader()
    for tutorial in tutorials:
        csv_writer.writerow(tutorial)

    f.close()



if __name__ == "__main__":
    tutorials = read_csv_as_dict()
    print(tutorials)
    #tutorials.append({'tutorial':'F09A', 'tutor':'Kai', 'enrollments':21})
    write_dict_as_csv(tutorials)
