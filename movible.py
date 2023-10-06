'''  
Esta liberia sirve para generar mediante Matplotlib un display interactivo
donde los puntos que aparecen en pantalla se pueden mover con arrastrandolos mientras
se presiona el CLICK IZQUIERDO, los valores de los puntos se se actualizarane el
archivo "points.txt" que es el que controla cuantos y puntos estan en juego y sus 
posiciones iniciales. 


NOTA: ESTA LIBRERIA FUE OBTENIDA DE UN SERVIDOR EN LINEA SOLAMENTE PARA TENER UNA 
CLASE DE PUNTOS MOVIBLES EN UNA GRÁFICA. LO DEMÁS FUE IMPLEMENTADO POR NOSOTROS
'''
import numpy as np
import matplotlib.pyplot as plt
import bezier_calculate as bzc
import bezier_plot as bzp


class DraggableScatter(): #Clase de puntos arrastables

    epsilon = 5
    def __init__(self, scatter, ax1):

        #Asignamos la tabla de puntos 
        self.scatter = scatter
        self._ind = None
        self.ax = scatter.axes #Asignamos los ejes
        self.ax1 = ax1 #Asignamos la figura en general 
        self.canvas = self.ax.figure.canvas
        self.canvas.mpl_connect('button_press_event', self.button_press_callback) #Detecta si presionamos un punto para mover 
        self.canvas.mpl_connect('button_release_event', self.button_release_callback) #Detecta cuando soltamos un punto 
        self.canvas.mpl_connect('motion_notify_event', self.motion_notify_callback) 
        plt.show()


    #Con esta funcion obtenemos el indice del punto con el que estamos interactuando
    def get_ind_under_point(self, event):   
        xy = np.asarray(self.scatter.get_offsets())
        xyt = self.ax.transData.transform(xy)
        xt, yt = xyt[:, 0], xyt[:, 1]

        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()

        if d[ind] >= self.epsilon:
            ind = None

        return ind

    def button_press_callback(self, event):#FUNCION QUE DETECTA CUANDO SE SELECCIONA
        if event.inaxes is None:           #UN PUNTO CON EL MOUSE
            return
        if event.button != 1:
            return
        self._ind = self.get_ind_under_point(event)
        
        


    def button_release_callback(self, event): #FUNCION QUE DETECTA CUANDO SE SUELTA 
        if event.button != 1:                 #EL MOUSE SOBRE UN PUNTO
            return
        self._ind = None
          

    def motion_notify_callback(self, event):#ESTA FUNCION GRACIAS A LA LOGICA DE LAS 
        if self._ind is None:               #DOS ANTERIORES, REALIZA ACCIONES O NO
            return                          #CUANDO ESTAMOS PRESIONANDO UN Y MOVIENDO
        if event.inaxes is None:            #UN PUNTO, 
            return
        if event.button != 1:
            return
        x, y = event.xdata, event.ydata
        
        xy = np.asarray(self.scatter.get_offsets())
        xy[self._ind] = np.array([x, y]) 

        #Nosotros implementamos esta parte para reescribir los puntos de control una vez que el usuario los mueve 
        with open("points.txt",'r') as f:
            get_all=f.readlines()

        with open("points.txt",'w') as f:#Nos posicionamos en el punto correcto y reescribimos el punto con el formato deseado 
            for i,line in enumerate(get_all):             
                if i ==  self._ind:    
                    spoint = f"{x},{y}\n"                          
                    f.writelines(spoint)
                else:
                    f.writelines(line)

        
        #Dibujamos los puntos 
        self.scatter.set_offsets(xy)
        self.canvas.draw_idle()

       #Ahora volvemos a generar los puntos de la curva y los graficamos para que la curva se modifique si movemos un punto o varios 
        bzc.BezeirPoints(25, 200).generate()
        bzp.PLOT_BEZIER(self.ax1)

        