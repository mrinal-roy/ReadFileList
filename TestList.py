import os
Location = str(input("Enter the location of the files:"))
os.chdir(Location)
with open(os.path.join(Location,'FileList.txt'),'w') as fL:  #Creates a file named FileList.txt where list of files is written
    for g in os.listdir(Location):
        if g!='FileList.txt':       # this eliminates the FileList.txt from the list of files
            Size = (os.path.getsize(g))/1000
            # Time = (Size *257)/5.3
            # S = round((Time%60),1)
            # M = (Time//60)
            F_Size=round(Size,1)
            fL.write(g + " - " + str(F_Size) + "kB - ")
            fL.write("\n")
