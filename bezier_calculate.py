'''
Definimos funciones y una clase para calcular los puntos de la curva de Bezier. Ahora, definiremos la curva de Bezier B de grado n como 

                        B(t) = Σ_{i} B_i b_{i, n}(t)

donde 
                        b_{i, n}(t) = binom(n, i) (1 - t)^{n - i} * t^i
                                                
'''



import pandas as pd
import math
import time


def nCr(n,r): #Calculamos el coeficiente binomial C(n,r)
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def c(k, n, t): # Base polinomial de Berstein
    return nCr(n,k)*(t**k)*((1-t)**(n-k))

class BezeirPoints():  #clase de para la manipulacion y control de los puntos de Bezier
    def clear_file(self): #Borramos el documento donde se guardaran los puntos de beizer
        with open("bpoints.txt",'w+') as handle:
            handle.write("")

    def __init__(self, interval, speed ): #interval es el numero de puntos de Bezier. Mayor el intervalo, obtenemos mayor resolucion de la curva 
        self.speed = speed                #Que se van a graficar, y Speed es la velocidad
        self.control_points = pd.read_csv('points.txt', header=None) #Con la que se Plotea
       
        if self.control_points.shape[1] != 2:                        #La grafica (Curva de Bezier)
            print("\n!! NO SON ELEMENTOS DE R2 !!\n") #Checamos que los puntos a graifcar pertenezcan a R2
            return 
       
        self.n = self.control_points.shape[0] - 1 #Definimos el numero de puntos de control 
        self.interval = interval  
        self.clear_file() #Antes de escribir cualquier punto, limpiamos el archivo 

    #Declaramos una funcion para escrirbir en el archivo
    def write_file(self,point): #Recibe como parametro el punto a escribir 
        with open('bpoints.txt', 'a') as f:
            spoint = f"{point[0]},{point[1]}\n" #Separamos con una coma 
            f.write(spoint)

    #Con esta funcion generamos el calculo de los puntos de la curva 
    def generate(self):
        n = self.n
        df = pd.DataFrame()
        for t in range(self.interval+1):
            t = t/self.interval
            bpoint = [0, 0]
            for k in range(n+1):
                pk = self.control_points.iloc[k] #Obtenemos el par coordenado
                constant = c(k, n, t) #Calcualmos la constante
                bpoint[0] += pk[0]*constant #Hacemos el calculo de cada punto 
                bpoint[1] += pk[1]*constant
            bpoint[0] = "{:.2f}".format(bpoint[0])
            bpoint[1] = "{:.2f}".format(bpoint[1])
            self.write_file(bpoint) #Escribimos el punto en el archivo txt 
            time.sleep(1/self.speed)
