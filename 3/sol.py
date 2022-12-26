#objectif trouver lettre commun et sommer points 
#ouvrir fichier 
#compter nombre lettre par ligne et diviser par deux
# rentrer dans deux listes différentes 
# pour chaque caractere d'un sac demander si in liste 2 si oui compter ses points dans la somme totale  

def common(l1,l2):
    for a in range(len(l1)):
        if l1[a] in l2 and l1[a] not in l1[:a]:
            return l1[a]
    return ''

def score (e):
    S=0
    if e.upper()==e:
        S+=ord(e)-38
    else:
        S+=ord(e)-96
    return S

def common2(l1,l2, l3):
    for a in range(len(l1)):
        if l1[a] in l2 and l1[a] in l3 and l1[a] not in l1[:a]:
            return l1[a]
    return ''

def main():
    with open('input') as f:
        lines=f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    print(lines)


    s=0
    for i in range(len(lines)):
        n = len(lines[i])
        l1=lines[i][:n//2]
        l2=lines[i][n//2:]
        e = common(l1, l2)
        s+=score(e)
    print(s)

    s=0
    for i in range(0, len(lines), 3):
        l1=lines[i]
        l2=lines[i+1]
        l3=lines[i+2]
        e=common2(l1,l2,l3)
        s+=score(e)

    print(s)    

main()