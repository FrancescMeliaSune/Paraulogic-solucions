# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:04:07 2022

@author: meliasun
"""
# %% LLibreries
import os
import pickle
os.chdir(r'C:\Users\meliasun\OneDrive\Documents\Zeng docs\Proves Python\meus\paraulogic')

# %% Carrregar fitxer per tenir variabl preparada per a analitzar

# Open the file in binary mode
with open('fitxer_diccionari_arreglat.pkl', 'rb') as file:
    # Call load method to deserialze
    diccionari = pickle.load(file)
    print(diccionari)
del(file)

# Diccionari de prova diccionari = ['ordinador','got','gotet','lalaland','movil']
# Lletres de prova: l_centre = 'g'; l_perif1 = 'o'; l_perif2 = 't'; l_perif3 = 'e'; l_perif4 = 'z'; l_perif5 = 'n'; l_perif6 = 'y'

#%% Funcions

# Crear llista de paraules que cumpleixen les 3 condicions (longitud major o igual a 3 i lletra central està a candidat i lletres de candidat estàn a hegàgon)
def poblarLlista(diccionari, l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6):
    outputList = []
    for paraula in diccionari:
        if cumpleixTresCondicions(paraula, l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6):
            outputList.append(paraula)
    return outputList

# Cumpleix 3 condicions ?
def cumpleixTresCondicions(paraula, l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6): # https://stackoverflow.com/questions/35101426/how-to-return-a-subset-of-a-list-that-matches-a-condition
    bool_cond1_cond2 = False
    if (len(paraula)>=3) and find_letter(l_centre,paraula): #https://www.w3schools.com/python/python_while_loops.asp
        bool_cond1_cond2 = True
        bool_cond_3 = True
        i=0
        while(i<len(paraula) and bool_cond_3): # https://stackoverflow.com/questions/41368066/str-object-has-no-attribute-len
            bool_cond_3 = find_letter(paraula[i],[l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6])
            i += 1
    return bool(bool_cond1_cond2 and bool_cond_3)

# Candidat té lletra central ?     # https://stackoverflow.com/questions/26355191/python-check-if-a-letter-is-in-a-list
def find_letter(letter, lst):
    return any(letter in word for word in lst)

# %% Execució i publicació
# l_centre = 'n'; l_perif1 = 'a'; l_perif2 = 'r'; l_perif3 = 'l'; l_perif4 = 't'; l_perif5 = 'g'; l_perif6 = 'o'
l_centre = 'i'; l_perif1 = 'o'; l_perif2 = 'c'; l_perif3 = 'u'; l_perif4 = 'b'; l_perif5 = 't'; l_perif6 = 's'

sortida = poblarLlista(diccionari, l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6)
# print(poblarLlista(diccionari, l_centre, l_perif1, l_perif2, l_perif3, l_perif4, l_perif5, l_perif6))