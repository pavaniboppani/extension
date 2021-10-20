filename = input("Input the Filename: ")

filename,separator,extension=filename.partition('.')

if(extension=='py'):
    print("The extension of the file is : 'python'")

elif(extension=='c'):
    print("The extension of the file is : 'C'")
    
elif(extension=='cpp'):
    print("The extension of the file is : 'C++'")

elif(extension=='java'):
    print("The extension of the file is : 'java'")
