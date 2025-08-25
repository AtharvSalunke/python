



try:
    f = open("demo.txt","w")

    try:
        f.write("hey there whatsupp")
        print("sucessfully written into file")


    except:
        print("Cannot write, there is some issue")

    finally:
        f.close()

except:
    print("File not found")

