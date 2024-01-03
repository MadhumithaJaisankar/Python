import os

print("current directory",os.getcwd())
os.chdir("D:\intern training\python\python basics")
print("changed directory",os.getcwd())

print("list of files and directories in cwd",os.listdir())

#creating new directory
#os.mkdir("direc_example")
print("list of directories",os.listdir())

#renaming a file/directory

#os.rename("direc_example","directory")
#print("after renaming",os.listdir())

#removing a directory

os.rmdir("directory")
print("after removing",os.listdir())