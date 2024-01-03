def product_except_i(_array):
    product=1
    product_array=[]
    for i in _array:
        product*=i
    for i in array:
        q=0
        p=product
        while p>=i:
            p-=i
            q+=1
        product_array.append(q)
        #value=product/i
        #product_array.append(value)
    print(product_array)


array=[]
n=int(input("enter the number of elements in the array"))
print("enter the array/list elements")
for i in range(n):
    x=int(input())
    array.append(x)
print(array)
product_except_i(array)