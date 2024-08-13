# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:22:16 2018

@author: gvandeyk
"""
import sys
import string

def ValideerLetter(letter):
    ValidatieFoutBoodschap = ' '
    if len(letter) > 1:
        letter = letter[0]
    for char in letter.upper():
        if char not in string.ascii_uppercase:
            ValidatieFoutBoodschap = ('Gebruik enkel letters [A-Z] ' + char +
                                      ' is niet toegelaten. ')
            raise TypeError(ValidatieFoutBoodschap)
    return letter.upper()


def ValideerWoord(woord):
    ValidatieFoutBoodschap = ' '
    for char in woord.upper():
        if char not in string.ascii_uppercase:
            ValidatieFoutBoodschap = ('Gebruik enkel letters [A-Z] ' +
                                      char + ' is niet toegelaten. ')
            raise TypeError(ValidatieFoutBoodschap)
        if len(woord) > 8:
            ValidatieFoutBoodschap = ('Het woord mag max. 8 letters ' +
                                      'lang zijn.' + woord + ' is ' +
                                      str(len(woord)) + ' letters lang.')
            raise TypeError(ValidatieFoutBoodschap)
        if len(woord) < 3:
            ValidatieFoutBoodschap = ('Het woord moet min. 3 letters ' +
                                      'lang zijn. ' + woord + ' is ' +
                                      str(len(woord)) + ' letters lang.')
            raise TypeError(ValidatieFoutBoodschap)
    return woord.upper()


def CheckWinstConditie(Opgave, GegevenOplossing):
    return (Opgave.upper() == GegevenOplossing.upper())


def main():
    VerderZoeken = True
    NuGokken = False
    while True:
        print('Kies een woord van 3 tot 8 letters lang (X om te stoppen) : ')
        SpelLeiderInput = input()
        #  Gebruiker koos ervoor te stoppen.
        if SpelLeiderInput == 'X':
            print(''' Tot ziens!!!''')
            sys.exit()
        #  Gebruiker koos ervoor om door te gaan.
        print('''U koos : ''', SpelLeiderInput)
        # Valideer input
        try:
            HetGezochteWoord = ValideerWoord(SpelLeiderInput)
            print(HetGezochteWoord)
            break
        except BaseException as e:
            print(''' Het door u gekozen woord is ongeldig : ''', str(e))
    WeergegevenWoord = ('_'*len(HetGezochteWoord))

    #  Hier begint het raden van het gezochte woord
    while(VerderZoeken):
        print(WeergegevenWoord + '\n( ' +
              str(len(HetGezochteWoord)) + ' letters )\n\n')
        if NuGokken:
            print('\nU mag een gokje wagen :')
            SpelerGok = input().upper()
            if CheckWinstConditie(HetGezochteWoord, SpelerGok):
                print('U heeft gewonnen : ')
                print('\nwij zochten ' + HetGezochteWoord)
                VerderZoeken = False
                break
        while True:
            print('''Kies een letter [A-Z]''')
            print('''kleine en hoofdletters worden beide aanvaard''')
            print('''(0 om te stoppen)''')
            SpelerInput = input()
            #  Gebruiker koos ervoor te stoppen.
            if (SpelerInput == str(0)):
                print('''Tot ziens!!!''')
                sys.exit()
            #  Gebruiker koos ervoor om door te gaan.
            print('''U koos : ''', SpelerInput)
            # Valideer input 1: is de input inderdaad een letter
            try:
                DeGekozenLetter = ValideerLetter(SpelerInput)
                break
            except BaseException as e:
                print(''' Het door u gekozen teken is ongeldig : ''', str(e))
        if DeGekozenLetter in HetGezochteWoord:
            IndexLetter = HetGezochteWoord.index(DeGekozenLetter)
            if IndexLetter == 0:
                WeergegevenWoord = DeGekozenLetter + WeergegevenWoord[1:]
            elif IndexLetter > 0:
                WeergegevenWoord = (WeergegevenWoord[:IndexLetter] +
                                    DeGekozenLetter +
                                    WeergegevenWoord[IndexLetter+1:])
            NuGokken = True
        else:
            print(DeGekozenLetter + ' zit niet in het gezochte woord.')
    print('\n\nTot ziens!')


main()





