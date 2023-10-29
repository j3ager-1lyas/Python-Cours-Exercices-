
for Number in range(100,1000):
    Hundreds = Number // 100
    Tens = (Number % 100) //10
    Units = (Number % 100) % 10
    if (Number == (Hundreds **3 + Tens**3 + Units ** 3)):
        print(Number)

