from math import sqrt,sin,cos,tan,radians                
def puissance():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return (nb1,nb2,round (nb1**nb2,2))
def racine_carre():
    nb=demande_Nombre()
    while nb<0: 
            print("le racine carré doit étre supérieur ou égal à 0!!")
            nb = demande_Nombre()
    return (nb,None,round(sqrt(nb),2))
def demande_Nombre():
    while True:
         nb= input("donner un nombre\n")
         try:
            nb=float(nb)
            return nb
         except ValueError:  
            print("Merci de saisir un nombre valide")
def addition():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return (nb1,nb2,round (nb1+nb2,2))
def difference():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return (nb1,nb2,round (nb1-nb2,2))
def produit():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return (nb1,nb2,round (nb1*nb2,2))
def quotient():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    while nb2==0: 
            print("le diviseur doit être différent à 0!!")
            nb2 = demande_Nombre()
    return (nb1,nb2,round (nb1/nb2,2))
def modulo():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    while nb2==0: 
            print("le reste de division doit être différent à 0!!")
            nb2 = demande_Nombre()       
    return (nb1,nb2,round (nb1%nb2,2))
def LireOp(): 
    op = input("Saisir l'opération: / * + - % ** rc care sin cos tan (si vous voulez quitter tapez q/quit)\n").strip().lower()
    if op in ["q", "quit"]:
        return None
    while op not in ["*", "+", "-", "/", "%", "**", "rc" , "care" ,"sin" , "cos" , "tan"]:
        print("Merci de saisir une opération valide")
        op = input("Saisir l'opération: / * + - % ** rc care sin cos  tan (q pour quitter)\n").strip().lower()
        if op in ["q", "quit"]: 
            return None
    return op
def carre():
    nb=demande_Nombre()
    return (nb, None, round(nb*nb,2))
def sinus():
    mesureAngle,angleRadian = demande_angle()
    return (mesureAngle, None, round(sin(angleRadian),2))
def cosinus():
    mesureAngle,angleRadian = demande_angle()
    return (mesureAngle, None, round(cos(angleRadian),2))
def tangente():
    mesureAngle,angleRadian = demande_angle()
    return (mesureAngle, None, round(tan(angleRadian),2))
def demande_angle():
    print("donner la mesure de l'angle en degrés")
    nb=demande_Nombre()
    return (nb,radians(nb))
operations={
    "+":addition,
    "-":difference,
    "/":quotient,
    "%":modulo,
    "*":produit,
    "rc":racine_carre,
    "**":puissance,
    "care":carre,
    "cos":cosinus,
    "sin":sinus,
    "tan":tangente
    }
historique=[]
while True :
        op = LireOp()
        if op is None :
            break
        L=[]
        L.append(op)  
        resultat = operations[op]()  
        L.extend(resultat)
        historique.append(L)
        print("le résultat vaut: ", resultat[2], "\n")
print("affichage de l'historique\n")
for operation in historique:
    if operation[2] is None:
        if operation[0] in ["cos","sin","tan"]:
            if operation[1].is_integer():
                print(operation[0], "(",int (operation[1]),"°)" "=", operation[3])
            else:
                 print(operation[0], "(",operation[1],"°)" "=", operation[3])
        elif operation[0] == "care":
             print ( "(",operation[1] ,")²=", operation[3])
        elif operation[0] == "rc" :
             print ( "√",operation[1] ,"=", operation[3])
    else:
         print(operation[1], operation[0], operation[2], "=", operation[3])
print("\n")
print("Merci pour l'utilisation de ma petite Calculatrice")
