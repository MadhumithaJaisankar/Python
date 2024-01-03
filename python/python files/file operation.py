print("I/O handling")
f= open("Examplefile.txt","w")
f.write("this is file")
f.close()
f= open("Examplefile.txt","r")
data= f.read()
print(data)
f.close()
f1= open("example2.txt","w")
lines=["line1\nline2\nline3\nline4"]
f1.writelines(lines)
f1.close()
f1=open("example2.txt","r")
line=f1.readline()
while line:
    print(line)
    line=f1.readline()
f1.close()

print("using with keyword")
with open("Examplefile.txt","a") as file:
    file.write("\nusing 'with' keyword to access the file")
with open("example2.txt","r") as file:
    print(file.read())        