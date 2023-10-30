from random import randint

while(True):
    SecretNumber=randint(1,10)
    for Tentative in range (1,3+1):
        Number = int(input("Entrer un nombre entre 1 et 10: "))
        if Number == SecretNumber:
            print("Bravo!!!")
            break
        else:
            if Number<7:
                print("Plus grand!")
            else:
                print("Plus petit!")
        if(Tentative == 3):
            print("Perdu!!!")
    Decision = input("Voulez-Vous jouer a nouveau si oui entrer oui: ")
    if(not(Decision == 'oui')):
        break

print("Merci et a bientot")