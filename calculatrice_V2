# Premier mini projet calculatrice
from math import sqrt,sin,cos,tan,radians                
def puissance():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return round(nb1**nb2,2)
def racine_carre():
    nb=demande_Nombre()
    while nb<0: 
            print("le racine carré doit étre supérieur ou égal à 0!!")
            nb = demande_Nombre()
    return round(sqrt(nb),2)
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
    return round (nb1+nb2,2)
def difference():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return round(nb1-nb2,2)
def produit():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    return round(nb1*nb2,2)
def quotient():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    while nb2==0: 
            print("le diviseur doit être différent à 0!!")
            nb2 = demande_Nombre()
    return round(nb1/nb2,2)
def modulo():
    nb1=demande_Nombre()
    nb2=demande_Nombre()
    while nb2==0: 
            print("le reste de division doit être différent à 0!!")
            nb2 = demande_Nombre()       
    return round(nb1%nb2,2)
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
    return round(nb*nb,2)
def sinus():
    angle=demande_angle()
    return round(sin(angle),2)
def cosinus():
    angle=demande_angle()
    return round(cos(angle),2)
def tangente():
    angle=demande_angle()
    return round(tan(angle),2)
def demande_angle():
    print("donner la mesure de l'angle en degrés")
    nb=demande_Nombre()
    return radians(nb)
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
while True :
    op = LireOp()
    if op is None :
        break
    resultat = operations[op]()   
    print("le résultat vaut: ", resultat, "\n")
print("Merci pour l'utilisation de ma petite Calculatrice")
 
