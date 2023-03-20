from itertools import combinations, permutations
from os import system
from time import sleep

tab = []

l = 0 # Taille des pw

style = open ( "style.txt", 'r' )

loop = True

while loop:
    system ( "clear" )
    print ( style.read () )

    print ( "\n" )
    print ( "The number of words given afterwards must be less than the size of the passwords\n" )

    l = int ( input ( "Give the size of the passwords: " ) )

    if l <= 1:
        print ( "\n\nThe size of the passwords must be less than 1" )
        sleep ( 5 )
    else:
        loop = False

loop = True

system ( "clear" )
choice = str ( input ( "1: List your words (separated by commas without spaces): \n" ) )

output = choice.split ( ',' )

tabOut = [ i for i in combinations ( output, l ) ]

file = open ( "comb.txt", 'w' )

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