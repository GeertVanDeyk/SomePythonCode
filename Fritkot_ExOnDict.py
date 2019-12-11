# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import string 
### Afprinten prijslijst
def printPrijslijst(dict_basis, dict_vlees, dict_saus) :
    print('Prijslijst\n\n')
    for basis in dict_basis.keys() :
        print(basis + ' - ' + dict_basis_ID_NAAM[basis] + '\n')
        for prijs in dict_basis[basis].keys():
          print('\t' + prijs + '--' + str(dict_basis[basis][prijs]))
        print('\n')  
    for vlees in dict_vlees.keys() :
          print(vlees + ' - ' + dict_vlees_ID_NAAM[vlees] + '---' + str(dict_vlees[vlees]))
    print('\n')   
    for saus in dict_saus.keys() :
        print (saus + '-' + dict_saus_ID_NAAM[saus])
        for prijs in dict_saus[saus].keys():
            print ('\t' + prijs + '---' + str(dict_saus[saus][prijs]))
        print('\n')
    print('BEDANKT VOOR UW BEZOEK') 



dict_item_class = dict([('s','saus'),('v','vlees'),('b','basis')])

dict_saus_ID_NAAM = dict([('s1','mayonaise'),('s2','pickles')])
saus_maat = ['potje','op']
saus_prijs = [1,0.7]
dict_saus_prijs = dict(zip(saus_maat,saus_prijs))
dict_saus = {saus : dict_saus_prijs for saus in dict_saus_ID_NAAM} 


dict_basis_ID_NAAM = dict([('b1','frites'), ('b2','kroketten')])
basis_maat = ['groot','medium','klein']
basis_prijs = [4, 3.5,3] 
dict_basis_prijs = dict(zip(basis_maat,basis_prijs))
dict_basis = { basis : dict_basis_prijs for basis in dict_basis_ID_NAAM }

dict_vlees_ID_NAAM = dict([('v1','sito'), ('v2','curryworst')])
vlees_prijs = (4, 3.5)
dict_vlees = dict(zip(dict_vlees_ID_NAAM, vlees_prijs))

printPrijslijst(dict_basis, dict_vlees, dict_saus)

# Bestellen

Bestelling = str(input('Voer uw bestelling in')).split()
Bestelling.sort()
Totaal_te_betalen = 0
for item in Bestelling:
   if item[:1] == 's':
      print(dict_saus_ID_NAAM[item] + ' - ' + str(dict_saus[item]['op']))
      Totaal_te_betalen = Totaal_te_betalen + dict_saus[item]['op']
   if item[:1] == 'v':
      print(dict_vlees_ID_NAAM[item] + ' - ' + str(dict_vlees[item]))
      Totaal_te_betalen = Totaal_te_betalen + dict_vlees[item]
   if item[:1] == 'b':
      print(dict_basis_ID_NAAM[item] + ' - ' + str(dict_basis[item]['groot']))
      Totaal_te_betalen = Totaal_te_betalen + dict_basis[item]['groot']
print('\n')
print('Totaal te betalen ----------------- ' + str(Totaal_te_betalen) )


    

