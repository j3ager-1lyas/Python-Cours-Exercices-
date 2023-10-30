import math

NumberN=int(input("Entrer Un Entier N non nul:"))
if NumberN<=0:
    print("Le Nombre N doit etre strictement superieur a 0")
else:
    for NumberB in range(1,NumberN):
        for NumberA in range(1,NumberB):
            NumberC=NumberA**2 + NumberB**2
            if NumberC % math.sqrt(NumberC) == 0:
                if(math.sqrt(NumberC)<NumberN):
                    print(NumberA,",",NumberB,",",math.sqrt(NumberC))
                else:
                    NumberA = NumberB+1
