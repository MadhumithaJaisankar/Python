print("Operators in python")
print("arithmetic operators\nCalculation of area of rectangle")
lenght= 23
breadth= 52
area_rec= lenght*breadth
print("area of rectangle",area_rec)

print("calculation of area of a triangle")
height=29
area_tri=(breadth*height)/2
print("area of a triangle",area_tri) 

print("Calculation of sum of first 10 natural numbers")
sum=0
for i in range(10):
    sum=sum+i
print("the sum 10 natural numbers",sum)

print("computing the maximum of three numbers")
num1=int(input("enter an number"))
num2=int(input("enter an number"))
num3=int(input("enter an number"))
if (num1>num2) and (num1>num3):
    print("Number1 is the maximum of three numbers")
elif num2 > num1 and num2 > num3:
    print("Number2 is the maximum of three numbers")
else:
    print("Number3 is the maximum of three numbers")




