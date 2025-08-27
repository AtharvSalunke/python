
with open('demo.txt','w') as f:
    f.write('asdddddddddddd')
    f.close()


with open('demo.txt', 'r') as f:
    print(f.read())