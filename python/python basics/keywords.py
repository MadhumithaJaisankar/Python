#this is a comment line
class Keywords:
    def conditionalstmts(self,num1,num2,num3):
# computing the maximum of three numbers given
        if (num1>num2) and (num1>num3):
            print("Number1 is the maximum of three numbers")
        elif num2 > num1 and num2 > num3:
            print("Number2 is the maximum of three numbers")
        else:
            print("Number3 is the maximum of three numbers")

    
    def iterativestmts(self,num):
#printing only the odd numbers upto num
        i=0
        while i<num:
            if i%2==0:
                i+=1
                continue
            else:
                print(i)
            i+=1

    def Forloop(self):
#working of for loop and 'break' keyword
        Data = ["int","float","list","tuple","dictionary","string"]
        for i in Data:
            if i=="list":
                break
            print(i)

    def Exceptionhandling(self):
        divisor=5
#handling Arithmetic error
        try:
            result=10/(divisor-divisor)
        except ArithmeticError:
            print("Division by zero error")
        finally:
            print("something went wrong while dividing")
#raising an user-defined error
        try:
            raise Exception("something went wrong")
        except Exception:
            print("something did go wrong")

   
k1=Keywords()
print("use case of the keywords in python")
k1.conditionalstmts(5,7,4)
k1.iterativestmts(10) 
k1.Forloop()   
k2=Keywords()
k2.Exceptionhandling() 
#using lambda keyword to check whether a number is positive or not
Result=lambda number: True if number > 0 else False
print(Result(3))   
print(Result(-4))   

            
with open("Examplefile.txt","a") as file:
    file.write("\nusing 'with' keyword to access the file")
with open("example2.txt","r") as file:
    print(file.read())           





        