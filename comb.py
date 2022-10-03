from itertools import combinations, permutations
from os import system
from time import sleep

file = open ( "comb.txt", 'w' )
style = open ( "style.txt", 'r' )
tab = []

l = 0 # Taille des pw

loop = True

while loop:
    print ( "*********************************************************\n" )
    print ( style.read () )
    print ( "*********************************************************\n\n" )

    print ( "Ce logiciel a été créé et soumis par l'utilisateur à la license Apache 2.0\n" )

while loop:
    system ( "clear" )
    l = int ( input ( "Donner la taille des mots de passe: " ) )

    if l <= 1:
        print ( "\n\nLa taille des mots de passe doit être suppérieur à 1" )
        sleep ( 5 )
    else:
        loop = False

loop = True

system ( "clear" )
choix = str ( input ( "1: Donner la liste de vos mots (séparé par des virgules sans espaces): \n" ) )

output = choix.split ( ',' )

tabOut = [ i for i in combinations ( output, l ) ]

for i in tabOut:
    tabPermute = []
    j = 0
    memory = ""

    while j < l:
        memory += i [ j ]
        tabPermute.append ( i [ j ] )
        j += 1

    file.write ( memory + "\n" )

    tabPermute = [ y for y in permutations ( tabPermute, l ) ]

    for u in tabPermute:
        string = ""
        k = 0

        while k < l:
            string += u [ k ]
            k += 1
        
        if string != memory:
            file.write ( string + "\n" )

loop = False
file.close ()
style.close ()