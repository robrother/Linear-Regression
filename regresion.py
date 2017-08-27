import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
import numpy as np
from numpy import array
import cv2
import scipy
import math 
import pylab as pl


#numero de muestras
m=25
#x arm strenght
x = array([17.3, 19.3, 19.5, 19.7, 22.9, 23.1, 26.4, 26.8, 27.6, 28.1, 28.2, 28.7, 29.0, 29.6, 29.9, 29.9, 30.3, 31.3, 36.0, 39.5, 40.4, 44.3, 44.6, 50.4, 55.9])
#y dynamic Lift
y = array ([71.7, 48.3, 88.3, 75.0, 91.7, 100.0, 73.3, 65.0, 75.0, 88.3, 68.3, 96.7, 76.7,78.3, 60.0, 71.7, 85.0, 85.0, 88.3, 100.0, 100.0, 100.0, 91.7, 100.0, 71.7])
#xi*yi
xy = x * y
#xi^2
x2 = x * x
xi=x.sum()
yi=y.sum()
sxy=xy.sum()
sx2=x2.sum()
#a)
b1 = ((m*sxy)-(xi*yi))/((m*sx2)-(xi*xi))
b0 = (yi-b1*xi)/m
#b)
ytreinta = b0 + b1*30
s1 = 'El valor de B1 es '+ repr(b1)
s2 = 'El valor de B0 es '+ repr(b0)
s3 = 'El valor de uY para 30 es '+ repr(ytreinta)
print(s1)
print(s2)
print(s3)
########################------------Grafica----------------############################################
#x arm strenght
xg = np.array([17.3, 19.3, 19.5, 19.7, 22.9, 23.1, 26.4, 26.8, 27.6, 28.1, 28.2, 28.7, 29.0, 29.6, 29.9, 29.9, 30.3, 31.3, 36.0, 39.5, 40.4, 44.3, 44.6, 50.4, 55.9])
#y dynamic Lift
yg = np.array ([71.7, 48.3, 88.3, 75.0, 91.7, 100.0, 73.3, 65.0, 75.0, 88.3, 68.3, 96.7, 76.7,78.3, 60.0, 71.7, 85.0, 85.0, 88.3, 100.0, 100.0, 100.0, 91.7, 100.0, 71.7])

ygorro = b0 + b1*x
residual = y - ygorro
residual2 = np.array(residual)

#print 'El valor de y'
#print(y)
#print 'El valor de y gorro'
#print(ygorro)
#print 'El valor residual'
#print(residual)

#parametros de la grafica
plt.subplot(121)
xg2 = np.linspace(0,80,100)#los puntos para extender la linea desde el origen
pl.xlim(0.0, 70.0)#limites en x y y que seran mostrados
pl.ylim(0.0, 120.)
plt.xlabel('Arm Strenght',fontsize=20) #etiquetas en los ejes
plt.ylabel('Dynamic Lift',fontsize=20)
plot1 = plt.plot(xg2, b1*xg2 + b0, 'b',label='uY|x=B0 +B1x')
plot2 = pl.plot(xg, yg, 'ro',label='puntos')
plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.rc('grid', linestyle=":", color='black')
plt.grid(True)


plt.subplot(122)
plt.xlabel('Arm Strenght',fontsize=20)
plt.ylabel('Residual',fontsize=20)
plot3 = pl.plot(xg, residual2, 'bo',label='residuo')
plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.grid(True)
pl.show()
