import pandas as pd
import matplotlib.pyplot as plt
import statistics
from Ventana import Ventana

DATA = pd.read_csv('muertosactu.csv')# importando data
EDAD = DATA['EDAD'].sample(100,replace= True)# seleccionamos la columna
mediasMuestras = [ ] #vector
#DesEstandar = statistics.stdev(EDAD) # Desviacion estandar de la muestra inicial
for i in range(5000):

   Muestra = EDAD.sample(100, replace =  True)# Muestras aleatorias con reemplazo
   media = statistics.mean(Muestra)# media de cada muestra
   mediasMuestras.append(media) # agregamos a la lista de medias Muestrales


# histograma
plt.hist(mediasMuestras, color = 'blue', edgecolor = 'black',bins = 18)
# titulos para el histograma
plt.title('Histograma Bootstrap')
plt.xlabel('Edades ')
plt.ylabel('Numero de Fallecidos')
plt.show()
# intervalo de confianza al 95%
Media = statistics.mean(EDAD) # Media de la muestra Incial
EstandarError = statistics.stdev(mediasMuestras) # error estandar
# limites para la precisión si la estimación de la muestra
limInferior = Media-2*EstandarError
limSuperior = Media+2*EstandarError
# conversion de mediasMuestra a pandas
test = pd.Series(mediasMuestras)
# cuantiles para el intervalo por percentiles
p1 = test.quantile(0.025)
p2 = test.quantile(0.975)
# visualizacion de loss datos en una ventana
ventana =Ventana(str(p1.round(2)),str(p2.round(2)),
round(limInferior,2),round(limSuperior,2))

#grafica de densidad
pd.DataFrame(mediasMuestras, columns=['Edades']).plot(kind='density',
grid = True, title = "Grafica de densidad" ) # grafica de densidad


print(type(EDAD))