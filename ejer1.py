# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:42:38 2024

@author: ddiaz
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos= pd.read_csv("FIFA - 2022.csv", sep=",")
#Se calculs el ultimo cuartil que es la divison en 4 partes iguales de una lista de datos ordenados
def cuartil(x):
    for df in x.columns:
        print("El utimo cuartil de la columna",df," es",calc_cuartil(x[df]))
def calc_cuartil(x):
    x = x.sort_values()
    if len(x)%2!=0:
        result=(3*(len(x)+1))//4
        return x.iloc[result - 1]
    else:
        result=(3*len(x))//4
        return x.iloc[result - 1] 
#Se Calcula el percetil 80 que es la division entre 100 de un conjunto de datos ordenados,
# en este caso hallamos el dato que ocupa la pocision 80
def percentil(x):
    for df in x.columns:
        print("El percentil 80 de la clumna",df," es",calc_percentil(x[df]))
def calc_percentil(x):
    if len(x)%2!=0:
        x = x.sort_values()
        result=(80*(len(x)+1))//100
        return x.iloc[result - 1]
    else:
        x = x.sort_values()
        result=(80*len(x))//100
        return x.iloc[result - 1]

cuartil(datos)
print("------------")
percentil(datos)
print("Inciso B")

def cuartil_np(x):
    for co in x.columns:
        a=x[co]
        a=a.sort_values()
        d=np.percentile(a, 75)
        print("El ultimo cuartil de la clumna",co," con numpy es",d)

def persentil_np(x):
    for co in x.columns:
        a=x[co]
        a=a.sort_values()
        d=np.percentile(a, 80)
        print("El percentil 80 de la clumna",co,"es",d)
def media_np(x):
    for co in x.columns:
        a=x[co]
        a=a.sort_values()
        d=np.mean(a)
        print("La media de la clumna",co,"es",d)
        
def mediana_np(x):
    for co in x.columns:
        a=x[co]
        a=a.sort_values()
        d=np.median(a)
        print("La mediana de la clumna",co,"es",d)
def medianageo_np(x):
    for co in x.columns:
        a=x[co]
        a=a.sort_values()
        d=np.exp(np.mean(np.log(a)))
        print("La media geometrica de la clumna",co,"es",d)

print("Cuartil con numpy")
print(cuartil_np(datos))
print("Persentil con numpy")
print(persentil_np(datos))
print()
print("Inciso C")
print("Media con numpy")
print(media_np(datos))
print("Mediana con numpy")
print(mediana_np(datos))
print("Media geometrica con numpy")
print(medianageo_np(datos))
print()
print("Inciso D")
#percetil
data = datos["Win"]
data.sort_values()
la= np.percentile(data, 95)
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')
plt.axvline(la, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma ')
plt.legend(['Último percentil', 'Datos'])
plt.show()
#media
data = datos["Win"]
data.sort_values()
la= np.mean(data)
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')
plt.axvline(la, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma ')
plt.legend(['Media', 'Datos'])
plt.show()
#mediana
data = datos["Win"]
data.sort_values()
la= np.median(data)
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')
plt.axvline(la, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma ')
plt.legend(['Mediana', 'Datos'])
plt.show()
#media geometrica
data = datos["Win"]
data.sort_values()
la= np.exp(np.mean(np.log(data)))
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue')
plt.axvline(la, color='red', linestyle='dashed', linewidth=1)
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Histograma')
plt.legend(['Media geometrica', 'Datos'])
plt.show()






