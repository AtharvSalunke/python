# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

with open("abc.txt", "x+") as f:   # 'x+' = create + read/write, error if exists
    f.write("apple is a cat")
    f.seek(0)  # this resets the pointer to begining
    print(f.read())
    f.close()


