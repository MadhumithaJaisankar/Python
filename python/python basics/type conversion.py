print("Implicit type conversion")
num1=int(input("enter an integer number"))
num2=float(input("enter an floating point number"))
sum= num1+ num2
print(sum)
print(type(sum))


print("Explicit type conversion")
floating_num= float(num1)
print(floating_num)
print(type(floating_num))

integer_num=int(num2)
print(integer_num)
print(type(integer_num))

string_data= str(sum)
print(string_data)
print(type(string_data))
