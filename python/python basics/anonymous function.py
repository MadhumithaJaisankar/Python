print("anonymous funtion")
result= lambda number: "positive"if number>0 else "negative"

number=int(input("enter a number"))
print(result(number))