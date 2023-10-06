'''
Con las funciones de archivo .py somos capaces de graficar la curva bezier dado los puntos de control que se 
encuentran en un .txt llamada points y los puntos de la curva se encuentran en el txt llamado bpoints. Los puntos 
se calculan con funciones del archivo bezier_calculate.py

'''



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def points(): #Funcion que recoleta los puntos de control de un archivo .txt con el nombre
    control_points = pd.read_csv('points.txt', header=None)#points.txt
    return (                                               #Ese archivo en cuestion
            int(control_points.max().max()+1),             #se puede utilizar para 
            int(control_points.min().min()-1),             #para obtener el min y max
            control_points,                                # de cada eje X,Y y tener una
                                                           #Grafica mejor ajustada
            )

#Esta funcion recibe como parametro la variable de la grafica para poder graficar los puntos dado el archivo bpoints 
def PLOT_BEZIER(ax1):
    lines = open("bpoints.txt",'r').readlines() #Leemos linea por linea y los guardamos en una lista
    xs = [] #Definimos listas para cada valor de x y de y 
    ys = []

    #Vamos a iterar sobre lines para insertar cada valor en las listas correspondientes
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',') #Tenemos que considerar las comas de separacion 
            xs.append(float(x))
            ys.append(float(y))
    

    ax1.lines.clear() #Esto es para borrar la inmediata grafica anterior, esto ayuda
    #a crear el efecto de una ajuste en tiempo real de cada curva de bezier a mover 
    #los puntos de control
    max, min, control_points = points()



    axes = plt.axes() #Asignamos los valores minimos y maximos para nuestros ejes del graficador 
    axes.set_xlim([min,max])
    axes.set_ylim([min,max])
    color =  np.array([0.7,0,0.5])
    ax1.plot(xs, ys, c=color, linewidth=1) #Graficamos los puntos de la curva de bezier 


    
   
