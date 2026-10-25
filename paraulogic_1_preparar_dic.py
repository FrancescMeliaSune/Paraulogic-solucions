# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:39:44 2022

@author: meliasun
"""
# %% lllibreries
import os
import re # https://docs.python.org/3/library/re.html
import pickle
# %% Carregar fitxer
# change to folder where dic is stored
os.chdir(r'C:\Users\meliasun\OneDrive\Z\Zeng docs\Proves Python\meus\paraulogic\diccionaris')
    
# loading and reading the file in read mode
my_file = open("ca - Copy.txt","r", encoding="utf8") # https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca#46011113
data = my_file.read()
my_file.close()

# %% Arreglar variable
# tot a minúscules data = data.casefold() # https://www.w3schools.com/python/python_ref_string.asp

# reconvertir caràcters amb accents, tildes i punts flotants
# https://www.w3schools.com/python/ref_string_replace.asp
data = data.replace('à','a'); data = data.replace('è','e'); data = data.replace('é','e'); data = data.replace('í','i'); data = data.replace('ò','o'); data = data.replace('ó','o'); data = data.replace('ú','u')
data = data.replace('ç','c'); data = data.replace('ï','i'); data = data.replace('ü','u'); data = data.replace('·',''); data = data.replace('-','')

# idem, pero amb les majúscules
data = data.replace('À','a'); data = data.replace('È','e'); data = data.replace('É','e'); data = data.replace('Í','i'); data = data.replace('Ò','o'); data = data.replace('Ó','o'); data = data.replace('Ú','u')
data = data.replace('Ç','c'); data = data.replace('Ï','i'); data = data.replace('Ü','u')

# treure símbols del final de cada linia
data = re.sub('/.*?\n',"\n", data) # alt. = re.sub('/.+?\n',"\n", data) # https://stackoverflow.com/questions/8784396/how-to-delete-the-words-between-two-delimiters

# convert files (objectis a 'str') into a list, by replacing end splitting the text when newline ('\n') is seen.
data = data.split("\n") # https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/

# print(data)

# %% guardar en una variable https://www.geeksforgeeks.org/how-to-use-pickle-to-save-and-load-variables-in-python/
os.chdir(r'C:\Users\meliasun\OneDrive\Z\Zeng docs\Proves Python\meus\paraulogic')
# Open a file and use dump()
with open('fitxer_diccionari_arreglat.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(data, file)
del(data, my_file, file)