4 lines (4 sloc)  122 Bytes
   
filename = input("Enter a filename : ")
position = filename.rfind(".")
extension = filename[position:]
print(extension)