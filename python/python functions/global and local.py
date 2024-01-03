def global_local():
    number=10   #local variable
    print("inside function",number)
    global number2    #use of global 
    print("inside function",number2)

number=20
number2=40
print(number,"outside function")
print(number2,"outside function")      #global variable
global_local()
