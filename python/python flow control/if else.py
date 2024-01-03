print("python if..else")
studied=input("enter true or false")
if studied==True:
    print("you'll pass")
else:
    print("its hard to pass")

print("python if elif else")
mark=int(input("enter your mark"))
if mark>90:
    print("grade A")
elif mark>70 and mark<90:
    print("grade B")
elif mark>50 and mark<70:
    print("grade C")
else:
    print("fail :(")