#!/usr/bin/env python
# coding: utf-8

# # Shaar - Steen - Papier spel

# 1. need a randomizer to make the computer play
# Use randint so integer can be used as an index for a list element

# In[ ]:


from random import randint


# 2. need a function to decide on the winner
# 
# rules implemented:
#     rock > scissors
#     paper > rock
#     scissors > paper
# 
# Using a list of elements avoids having to test all possible combinations
# if weapon1 = p/r/s and weapon2 = p/r/s
# 
# Note: draw games are not tested for here

# In[ ]:


def decideWhoIsTheWinner(weapon1, weapon2):
    WeaponsUsed = [weapon1, weapon2]
    if 'r' in WeaponsUsed and 's' in WeaponsUsed :
        return 'r'
    if 'r' in WeaponsUsed and 'p' in WeaponsUsed :
        return 'p'
    if 'p' in WeaponsUsed and 's' in WeaponsUsed :
        return 's'


# 3. Need a dictionary of weapons
# This allows for the key (r/p/s) to be used in play, but for the full name to be returned in feedback from system

# In[ ]:


dictWeapons = { 'r':'rock', 'p' : 'paper','s' : 'scissors' }


# 4. Need a list of weapons for the computer to play with
# The list of weapons is build from the keys of the dictionary

# In[ ]:


ListWeapons = [key for key in dictWeapons.keys()]


# 5. Player and computer need to play
# a. player chooses his weapon (r/p/s)
# b. for the computer a random value is picked from the list of weapons 
#    using a random index from 0 to the (length of the list) - 1 

# In[ ]:


player = input('Choose your weapon - rock (r), paper (p), scissors (s) : ' )


# In[ ]:


computer = ListWeapons[randint(0,len(ListWeapons) - 1)]


# 6. the result of each decision is displayed on screen 
# the description values from the dictonary are used, based on the r/p/s key values

# In[ ]:


print(dictWeapons[player] +  ' vs ' + dictWeapons[computer])


# 7. if decisions are different (no draw game) the function decideWhoIsTheWinner is called

# In[ ]:


if player != computer :
    print(dictWeapons[decideWhoIsTheWinner(player,computer)] + ' wins!')
else:
    print('No winner!')

