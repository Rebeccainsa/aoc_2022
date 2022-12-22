#ouvrir input et lire et stocker dans liste 
#créer une liste :  nombre cal total pour chq lutin
#sommer cal --> if saut de ligne changer de lutin sinon sommer , et ajouter résultat dans classe 
#trouver le max--> parcourir liste en associant valeur plus grande 

with open('input') as f:
    lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].replace("\n","")
        if lines[i]=="":
            lines[i]=-1
        lines[i]=int(lines[i])
print(lines)
        
somme=[]
s=0

for x in lines:
    if x != -1:
        s=s+x
    elif x==-1:
        somme.append(s)
        s=0
somme.append(s)
print(somme)

max1=0
max2=0
max3=0
for x in somme:
    if x>max1:
        max1=x
print(max1)

for x in somme:
    if x>max2 and x<max1:
        max2=x
print(max2)

for x in somme:
    if x>max3 and x<max1 and x<max2:
        max3=x
print(max3)

print(max1+max2+max3)

#UTILISER UNE FONCTION POUR TRIER SOMMES CROISSANT 'sorted'


