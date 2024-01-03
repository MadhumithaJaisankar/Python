print("printing patterns using for loop")
rows=int(input("enter the number of rows"))
for i in range(rows):
    for j in range(i):
        print(i,end=' ')
    print(' ')

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
