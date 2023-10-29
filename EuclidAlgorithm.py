a = int(input("Entrer un Nombre a: "))
b = int(input("Entrer un Nombre b: "))
while(True):
    
    r = a % b
    a = b
    b = r
    if b == 0 : 
        print(a)
        break
