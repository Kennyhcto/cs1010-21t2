"""
Reading and Writing Plain Text Files

* How to know where the files will save?
* What happens if you don't close a file?
* What happens if the folder/file doesn't exist?
"""


def get_sample_data():
    return ["hello", "how are you?", "that's good",
            "nice to meet you", "goodbye\nI'll see you again"]


def write_file(data):
    # open file
    f = open('files/1_data.txt', 'w')

    # write contents
    for text in data:
        f.write(text + '\n')

    # close file
    f.close()


def read_file():
    # open
    f = open('files/1_data.txt', 'r')

    # read the contents
    data = []
    for line in f.readlines():
        data.append(line.strip())

    # close the file
    f.close()

    return data


if __name__ == "__main__":
    #data = get_sample_data()
    #write_file(data)

    my_data = read_file()
    print(my_data)
