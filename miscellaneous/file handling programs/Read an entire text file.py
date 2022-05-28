# Write a Python program to read an entire text file.

def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt') #First you need to create a file named test.txt and write something in it.
