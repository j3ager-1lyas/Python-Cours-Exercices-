print("This is Form1")
NumberL= int(input("Entrer Un Nombre de ligne:"))
if NumberL>= 1 and NumberL<=9:
    for Line in range(1,NumberL+1):
        for Column in range(1,Line+1):
            print(Column,end="")
        print("")
else:
    print("Number de Ligne doit etre entre 1 et 9")
#________________________________________________
print("This is Form 2")

NumberL= int(input("Entrer Un Nombre de ligne:"))
if NumberL>= 1 and NumberL<=9:
    for Line in range(1,NumberL+1):
        for Column in range(1,Line+1):
            print(Line,end="")
        print("")
else:
    print("Number de Ligne doit etre entre 1 et 9")
#__________________________________________________
print("This is Form 3")

NumberL= int(input("Entrer Un Nombre de ligne:"))
if NumberL>= 1 and NumberL<=9:
    for Line in range(1,NumberL+1):
        for Column in range(1,Line+1):
            print("*",end="")
        print("")
else:
    print("Number de Ligne doit etre entre 1 et 9")

#__________________________________________________
print("This is Form 4")

NumberL= int(input("Entrer Un Nombre de ligne:"))
if NumberL>= 1 and NumberL<=9:
    for Line in range(1,NumberL+1):
        for Space in range(1,NumberL-Line+1):
            print(" ",end="")
        for Column in range(1,Line-1):
            print("*",end="")
        for Column in range(1,Line+1):
            print("*",end="")
        for Space in range(1,NumberL-Line+1):
            print(" ",end="")
        print("")

else:
    print("Number de Ligne doit etre entre 1 et 9")
#___________________________________________________

print("This is Form 6")

NumberL= int(input("Entrer Un Nombre de ligne:"))
if NumberL>= 1 and NumberL<=9:
    for Line in range(1,NumberL+1):
        if Line == 1 or Line == NumberL:
            for Column in range(1,NumberL+1):
                print("*",end="")
        else:
            print("*",end="")
            for Column in range(2,NumberL):
                print(" ",end="")
            print("*",end="")
        print("")
else:
    print("Number de Ligne doit etre entre 1 et 9")