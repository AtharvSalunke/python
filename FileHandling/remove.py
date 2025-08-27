
# os is a module in Python that provides a way of
# using operating system dependent functionality like reading or writing to the file system.
# it can aslo remove folder just put os.remove('myfolder')
import os


try:
    os.remove('pqr.txt')
    print('successfully removed')

except FileNotFoundError:
    print("where the fuck is file")