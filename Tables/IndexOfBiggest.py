print("Ce Programme va afficher l'indice du plus grand Cellule de Tableau")
print("Premierement Saisir 10 Nombre Entier")

Tab=[]

for i in range(9+1):
    Tab.append(int(input(f"Entrer Un Nombre de la Cellule Tab[{i+1}]: ")))
    if i==0 :
        Biggest=i
    elif Tab[i]>Tab[Biggest]:
        Biggest=i

print("Les 10 Nombre Entier sont: ")

for i in range (9+1):
    print("Tab[",i,"]: ",Tab[i])

print("L'indice de plus grand Cellule est : ",Biggest+1,"La Cellule est Tab[",Biggest+1,"]= ",Tab[Biggest])
