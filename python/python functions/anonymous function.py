print("anonymous funtion to check whether the number is positive or not")
result= lambda number: "positive"if number>0 else "negative"
number=int(input("enter a number"))
print(result(number))