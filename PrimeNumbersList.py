
Number = int(input("Entrer un entier : "))
print("Les nombres premiers <= ",Number, " sont: ")
if Number > 1:

    for Counter1 in range (2,Number+1):
        Prime = True
        for Counter2 in range(2,Counter1):
            if (not(Counter1 % Counter2)):
                Prime = False
                Counter2 = Counter1+1
        if Counter1 == 2 :
            Prime = True
        if(Prime):
            print(Counter1)


