def quitter(q):
        if(q=="Q" or q=="q" or q=="quit" or q=="Quit"):
            while True:
                q=input("Vous voulez vraiment quitter l'application? o/n\n")
                if(q=="o"):
                    return True
                elif(q=="n"):
                    return False
                else:
                     print("Merci de saisir o/n\n")
        return False
def demandeNombre():
    while True:
         nb= input("donner un nombre\n") 
         try:
            nb=float(nb)
            return nb
         except:  
            print("Merci de saisir un nombre valide")
def addition(nb1,nb2):
    print ("Tu cherches la somme de ", nb1,"et ",nb2,": \n -->La résultat vaut ",nb2+nb1) 
def difference(nb1,nb2):
    print ("Tu cherches la différence entre ", nb1,"et ",nb2,": \n -->La résultat vaut ", nb1-nb2)
def produit(nb1,nb2):
    print ("Tu cherches le produit de ", nb1,"et ",nb2,": \n -->La résultat vaut ", nb1*nb2)
def quotient(nb1,nb2):
    while(nb2==0):  
            print("le diviseur doit être différent à 0!!")
            nb2 = demandeNombre()          
    nb3=round(nb1/nb2,2)
    print("Tu cherches le quotient de ", nb1,"par ",nb2,":\n --> La résultat vaut ", nb3)
def modulo(nb1,nb2):
    while(nb2==0): 
            print("le reste de division doit être différent à 0!!")
            nb2 = demandeNombre()          
    nb3=round(nb1%nb2,2)
    print("Tu cherches le reste de division de ", nb1,"par ",nb2,":\n --> La résultat vaut ", nb3)
def LireOp(op): 
    while(op!="*" and op!="+" and op!="-" and op!="/" and op!="%"):  
            if(quitter(op)):
              return None
            print("Merci de saisir une opération valide")  
            op = input(" Saisir l'opération à exécuter: / * + - %\n")
    return op
while True :
    op = input(" Saisir l'opération à exécuter: / * + - %\n")  
    op=LireOp(op)
    if op==None:
        break
    nb1=demandeNombre()
    nb2=demandeNombre()
    if op=="+": #les opération mathématique
        addition(nb1,nb2)
    elif op=="-":
        difference(nb1,nb2)
    elif op=="*":
        produit(nb1,nb2)
    elif op=="/": 
        quotient(nb1,nb2)
    else:
        modulo(nb1,nb2)
print("Merci pour l'utilisation de ma petite Calculatrice")