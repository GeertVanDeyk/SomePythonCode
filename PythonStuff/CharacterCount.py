# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:52:24 2018

@author: gvandeyk
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


mymessage = '''
This is the excellent foppery of the world, that,
when we are sick in fortune, often the surfeit of our own behaviour,
we make guilty of our disasters the sun, the moon, and the stars;
as if we were villains on necessity;
fools by heavenly compulsion; knaves, thieves,
and treachers by spherical pre-dominance; drunkards, liars, and adulterers
by an enforc'd obedience of planetary influence; and all that we are evil in,
by a divine thrusting on.
An admirable evasion of whore-master man,
to lay his goatish disposition to the charge of a star!
My father compounded with my mother under the Dragon's Tail,
and my nativity was under Ursa Major, so that
it follows I am rough and lecherous. Fut!
I should have been that I am,
had the maidenliest star in the firmament twinkled on my bastardizing.'''

TextAnalysis_dict = {}
print(mymessage)

for chars in mymessage:
    if chars.isalpha():
        character_UC = chars.upper()
        TextAnalysis_dict.setdefault(character_UC, 0)
        TextAnalysis_dict[character_UC] = TextAnalysis_dict[character_UC] + 1
TextAnalysis_dict_sorted = dict(sorted(TextAnalysis_dict.items()))
# for k, v in TextAnalysis_dict_sorted.items():
#    print(f'''{k} :  {v}''')

x = TextAnalysis_dict_sorted.keys()
y = TextAnalysis_dict_sorted.values()
plt.style.use('ggplot')
bar = plt.bar(x, y, 0.25)
plt.title('Occurrence of letters in a given text')
#  plt.xticks(x)
#  plt.yticks(y)
plt.xlabel('Letter')
plt.ylabel('Number of occurrences')
plt.show()



    