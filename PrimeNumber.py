
Number = int(input("Entrer un entier: "))
Prime = True
if Number <= 1 :
    Prime = False

for Counter in range(2, Number//2 +1):
    if (not(Number % Counter)):
        Prime = False
        Counter = Number

if Prime :
    print(Number," est premier")
else:
    print(Number , " n'est pas premier")