with open('demo.txt', 'a') as f:
    f.write("i appended it ")
    f.close()

# now see when i put 'a' it will add into exisitng data of file
# but when i do 'w' it will totally overwrite the file


with open('demo.txt', 'w+') as f:
    f.write("this is now overwritten")
    f.seek(0)
    print(f.read())
    f.close()