import os
import io
import numpy
from pandas import DataFrame

#This function to read the messages leaving the header from each of the files and suming it
#to list for classification

def reading_Files(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message

#Below function to append the message and their particular classification

def dffromdirectory(path, classification): #dataframefromdirectory
    rows = []
    index = []
    for filename, message in reading_Files(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

