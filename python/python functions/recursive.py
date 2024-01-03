print("fibonacci series")
def fibonacci(terms):
    if terms<=1:
        return terms
    else:
        return fibonacci(terms-1) + fibonacci(terms-2)

term=int(input("enter the number of terms"))
if term<=0:
    print("invalid input")
else:
    for i in range(term):
        print(fibonacci(i))

        