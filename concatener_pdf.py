# -*- coding: utf-8 -*-
"""
@author: hbouia (Created on Fri Jan 20 10:24:44 2017 avec spyder python27)
"""

import os

from PyPDF2 import PdfFileMerger

# Récupérer la liste des fichiers du répertoire courant
files=sorted(list(os.walk('./content/pdf/'))[0][2])

# Sélectionner la liste des fichiers finissant par .pdf ou .PDF
pdfs=[x for x in files]

# Lister les fichiers pdf à fusionner
print("\nListe des fichiers fusionnés : \n")
for i,f in enumerate(pdfs):
    print('%2d : %s' % (i + 1, f))

# Fusionner les pdf du répertoire courant
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open("./content/pdf/"+pdf, 'rb'))
    
# Créer un répertoire "fusion_pdf" s'il n'existe pas déjà
try:
    os.mkdir(r'.\content\pdf\fusion_pdf')
except:
    pass

# './fusion_pdf/result.pdf' : fichier contenant les pdf fusionnés   
with open('./content/pdf/fusion_pdf/result.pdf', 'wb') as out:
    merger.write(out)

print("\nLes fichiers listés sont concaténés dans './content/pdf/fusion_pdf/result.pdf'\n")
