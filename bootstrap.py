import pandas as pd
import matplotlib.pyplot as plt
import statistics
from Ventana import Ventana

DATA = pd.read_csv('muertos.csv')# importando data
EDAD = DATA['EDAD']# seleccionamos la columna
mediasMuestras = [ ] #vector

for i in range(5000):

   Muestra = EDAD.sample(89, replace =  True)# Muestras aleatorias con reemplazo
   media = statistics.mean(Muestra)# media de cada muestra
   mediasMuestras.append(media) # agregamos a la lista de medias Muestrales
# hsitograma
plt.hist(mediasMuestras, color = 'blue', edgecolor = 'black',bins = 18)
# titulos para el histograma
plt.title('Histograma Bootstrap')
plt.xlabel('Edades ')
plt.ylabel('Numero de Fallecidos')
plt.show()
# intervalo de confianza al 95%
DesEstandar = statistics.stdev(EDAD) # Desviacion estandar de la muestra inicial

Media = statistics.mean(EDAD) # Media de la muestra Incial

EstandarError = statistics.stdev(mediasMuestras) # error estandar de la muestra inicial

# limites para la precisión si la estimación de la muestra coincide con el valor de toda la población

limInferior = Media-2*EstandarError
limSuperior = Media+2*EstandarError


print("limite inferior",round(limInferior,0),"limite superior",round(limSuperior,0))
test = pd.Series(mediasMuestras)
# cuantiles para el intervalo por percentiles
p1 = test.quantile(0.025)
p2 = test.quantile(0.975)

ventana =Ventana(str(p1.round(2)),str(p2.round(2)),round(limInferior,2),round(limSuperior,2))

pd.DataFrame(mediasMuestras, columns=['Edades']).plot(kind='density',grid = True, title = "Grafica de densidad" ) # grafica de densidad
print(type(DATA))