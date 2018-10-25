# -*- coding: utf-8 -*-
#import de la fonction random
import random
 
#fonction jeu permettant de dérouler le jeu et faisant appel aux autres fonctions
def jeu (): 
    print ("LE JEU DU NOMBRE MYSTERE")
    proposition ()
    rejouer()
#fonction permettant de prendre en compte le nombre de l'utilisateur et de comparer avec le nombre mystère    
def proposition ():
    # nombre à deviner créer aleatoirement 
    nbrmystere = random.randint (1,100)
#nombre proposé par l'utilisateur 
    nbrjoueur = int (input("A ton avis, quel est le nombre mystère: "))
#faire tant que le nombre proposé ne sera pas le même que le nombre créer aleatoirement
    while (nbrjoueur != nbrmystere): 
        if (nbrjoueur > nbrmystere):
            print ("c'est trop grand, essaye encore!")
        else:
            print ("c'est trop petit, essaye encore!")
        nbrjoueur = int (input("A ton avis, quel est le nombre mystère: "))
    
    print ("c'est gagné!!")
#fonction qui va permettre de rejouer en tapant o    
def rejouer(): 
    run = input ("veux-tu rejouer? (o=oui ou n=non): ")
    if (run == 'o'):
        jeu ()
    else:
         print("Merci d'avoir joué avec moi ;)!")
          
        
#exécuter le jeu
f = jeu ()
print (f)
