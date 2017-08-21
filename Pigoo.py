# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:50:02 2017

@author: carlos.arana
"""

import os
import urllib
import pandas

fuente = r'http://www.pigoo.gob.mx/dashboard/exportar/excel/exportar_consulta_excel.php?tipo=max'
archivo_local = r'D:\PCCS\01_Analysis\01_DataAnalysis\04_Agua\Docs\pigoo.csv'

def Pigoo():
        if not os.path.isfile(archivo_local):
            urllib.request.urlretrieve(fuente, archivo_local)
        dataset = pandas.read_csv(archivo_local, skiprows = 2, header=1)


dataset.head()

