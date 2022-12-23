#ouvrir input 
#créer deux listes 
#calculer points de la facon suivante :
    #si list2[i]=X et list1[i]=C on gagne 1+6 points 
    #si list2[i]=X et list1[i]=B on gagne 1+0 points
    #si list2[i]=X et list1[i]=A on gagne 1+3 points 
 

    #si list2[i]=Y et list1[i]=A on gagne 2+6 points 
    #si list2[i]=Y et list1[i]=B on gagne 2+3 points 
    #si list2[i]=Y et list1[i]=C on gagne 2+0 points 

    #si list2[i]= Z et list1[i]=A on gagne 3+0 points
    #si list2[i]= Z et list1[i]=B on gagne 3+6 points
    #si list2[i]= Z et list1[i]=C on gagne 3+3 points 
 
with open('input') as f:
    lines=f.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip()
print(lines)

l1=[]
l2=[]
for i in range(len(lines)):
    l1.append(lines[i][0])
    l2.append(lines[i][2])
print(l1,l2)
'''
punct=0
for i in range(len(l2)):
    if l2[i]=="X" and l1[i]=="C":
        punct=punct+7
    elif l2[i]=="X" and l1[i]=="B":
        punct=punct+1
    elif l2[i]=="X" and l1[i]=="A":
        punct=punct+4
    elif l2[i]=="Y" and l1[i]=="A":
        punct=punct+8
    elif l2[i]=="Y" and l1[i]=="B":
        punct=punct+5
    elif l2[i]=="Y" and l1[i]=="C":
        punct=punct+2
    elif l2[i]=="Z" and l1[i]=="A":
        punct=punct+3
    elif l2[i]=="Z" and l1[i]=="B":
        punct=punct+9
    elif l2[i]=="Z" and l1[i]=="C":
        punct=punct+6
print(punct)
'''

punct=0
for i in range(len(l2)):
    if l2[i]=="X" and l1[i]=="C":
        punct += 2
    elif l2[i]=="X" and l1[i]=="B":
        punct=punct+1
    elif l2[i]=="X" and l1[i]=="A":
        punct=punct+3
    elif l2[i]=="Y" and l1[i]=="A":
        punct=punct+4
    elif l2[i]=="Y" and l1[i]=="B":
        punct=punct+5
    elif l2[i]=="Y" and l1[i]=="C":
        punct=punct+6
    elif l2[i]=="Z" and l1[i]=="A":
        punct=punct+8
    elif l2[i]=="Z" and l1[i]=="B":
        punct=punct+9
    elif l2[i]=="Z" and l1[i]=="C":
        punct=punct+7
print(punct)







