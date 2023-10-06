'''
Parcial 2 - EDITOR INTERACTIVO DE CURVAS BEZIER

Integrantes:
    -Dan Heli Sanchez Muniz
    -Jafet Castaneda Cerdan

INTRODUCCION:

Las curvas de Bezier se utilizan en graficos por ordenador para dibujar formas, para animación y en muchos otros lugares.
Se denomina curvas de Bezier a un sistema que se desarrollo  para el trazado de dibujos tecnicos, en el diseño 
aeronautico y en el de automoviles. 

Existen dos algotirmos posibles para graficar curvas de Bezier, uno siendo el Algoritmo de Casteljau o con los Polinomios de Bernstein. 
En este proyecto se hizo uso de los polinomios de Bernstein. 

El concepto fundamental del algoritmo de de Casteljau es elegir un punto C en el segmento de línea AB tal que C divida el segmento de línea 
AB en una razon de u:1-u (es decir, la razón de la distancia entre A y C y la distancia entre A y B es u). 

Ahora, se ejecuta este .py, con python main.py. 

Con la herramienta es posible mover los puntos de control y visualizar la ruta que sigue la curva con respecto a los puntos de control. 

'''

#LAS LIBRERIAS UTLIZADAS
from matplotlib.widgets import Button #PERA PODER DESPLEGAR BOTONES
import matplotlib.pyplot as plt # LIBERIA PARA EL DISPLAY DE PLOT PRINCIPAL
import bezier_calculate as bzc #LIBRERIA DONDE ESTAN LOS METODOS NUMERICOS DE C. BEZIER
from matplotlib import style #  PARA DEFINIR EL COLOR DE FONDO DEL DISPLAY
import bezier_plot as bzp # LIBERIA CREADA POR NOSOTROS PARA EVALUAR LA CURVA DE BEZIER
import movible as mov #LIBERIA PARA PODER TENER PUNTOS MOVIBLES EN EL DISPLAY DE PLT
import pandas as pd # PARA AUMENTAR LA EFICIENCIA DE LA LECTURA DE DATOS
import numpy as np # HACER USO DE OPERACIONES MATEMATICAS MAS EFICIENTES


#Definimos el estilo de color del fondo de nuestro graficador. Notese que hacemos uso de matplotlib.pyplot.
style.use('dark_background')

#Inicializamos nuestra variables para obtener la grafica 
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#Comenzamos a leer los puntos de control para guardarlos en un arreglo usando pandas
control_points = pd.read_csv('points.txt', header=None)

#Llamamos a nuestra clase de Bezier para calcular los puntos de la curva usando Casteljau
bzc.BezeirPoints(30, 1500).generate()

#Dibujamos/Graficamos la curva que tenemos como predeterminada
bzp.PLOT_BEZIER(ax1)

#Funcion para dibujar la curva bezier a la hora de presionar un boton 
def DrawBezier(event):
    bzc.BezeirPoints(30, 1500).generate()
    bzp.PLOT_BEZIER(ax1)




#Funcion que dibuja las lineas de control de la curva de bezier por los puntos
def Lines(event):
    lines2 = open("points.txt", 'r').readlines() #Leemos los puntos de control
    #Creamos listas vacias para guardar las componentes de x y de y de los puntos (x,y)
    xpoint = []
    ypoint = []

    for line in lines2: #llenamos correspondientemente xpoint y ypoint
            x, y = line.split(',')
            xpoint.append(float(x))
            ypoint.append(float(y))

    #Unimos a pares los puntos P_i y P_i+1 mediante segementos de rectas
    for i in range(len(lines2) -1):
        x = np.linspace(xpoint[i],xpoint[i+1], 1000) #intervalo de cada recta
        m = (ypoint[i]-ypoint[i+1])/(xpoint[i]-xpoint[i+1]) #pendiente de la recta i-esima
        #plot de la i-esima recta
        ax1.plot(x, m*(x-xpoint[i])+ypoint[i],linestyle="--" ); 


#---------------------------------------------------BOTONES------------------------------------------------------------------------------------#

#BOTON PARA GRAFICAR
axprev = plt.axes([.75, 0.9, 0.15, 0.07]) #Posicion del boton en la ventana 
Bezier_curve = Button(axprev, 'BEZIER', color = 'black') #Definimos el boton
Bezier_curve.on_clicked(DrawBezier) #Lo relacionamos con la funcion de dibujar la curva 



#BOTON PARA TRAYECTORIA

axBotonlines = plt.axes([.59, 0.9, 0.15, 0.07]) #Posicion del boton para mostrar la trayectoria seguida 
Traye_Lines = Button(axBotonlines, 'Trayectoria', color = 'black')
Traye_Lines.on_clicked(Lines)



#Inicializamos una clase para mover los puntos de control y poder modificar la curva a nuestro querer. 
#Notemos que llamamos a la funcion scatter para graficar los puntos 
mov.DraggableScatter(ax1.scatter(control_points[0], control_points[1], c="b"), ax1)







