print("while loop")
rows=int(input("enter the number of rows"))
i=0
while i <= rows-1:
    j=0
    while j<i:
        print(' ',end=' ')
        j+=1
    k=i
    while k<= rows-1:
        print("*",end=' ')
        k+=1
    print()
    i+=1