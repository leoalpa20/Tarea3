# Tarea3
Tarea 3 Leonardo Alfaro B60224

## Archivo punto1.py
Este archivo muestra el codigo necesario para encontrar los parametros de mejor ajuste para la curva
para esto se carga el archivo csv con ayuda de numpy y se descarta el titulo asi como la primera columna
Se suman con ayuda de numpy las columnas en X y Y para encontrar la PMF
posteriormente se crea un linspace de 5 a 15 y de 5 a 25 para los valores de X y Y respectivamente
Se grafican las funciones y se descubre que se ajustan de mejor manera a la distribucion Gaussiana
por lo que se define una funcion llamada gaussian_dist para asi calcular los parametros del modelo.
Solo queda llamar a la funcion definida anteriormente y pasarle los parametros adecuados y nos retorna
los los valores numericos de los parametros que mejor se ajustan a los datos, en X y Y respectivamente.
[9.90484381 3.29944288]
[15.0794609   6.02693775]
Se omite el plt.show() pero se realizo con anterioridad para asi obtener los graficos que se piden en 
el ultimo punto de la tarea

## Archivo correlation.py
Para este archivo se nos pide calcular la correlacion, la cual de las presentaciones se calcula como 
la sumatoria de las multiplicaciones de los x por los y por su pobabilidad, esto se logra de manera muy 
facil con el otro archivo csv proveido el xyp.csv se lee el archivo con ayuda de numpy saltando la cabecera
se hace un sencillo for que recorre la totalidad del array y multiplica los valores a la vez que los va sumando
al final de este se imprime el resultado de la sumatoria y se obtiene el valor de: 149.54281000000012
## Archivo covariance.py
En este archivo hay varios puntos, se calcula la covarianza de manera un poco similar a la correlacion pues lo que
se hace es con un for hacer una sumatoria de los valores en x menos su promedio que se calcula gracias a numpy
esto se multiplica por y menos su promedio y todo esto va multiplicado por su probabilidad, se obtiene un valor
de covarianza de: 0.06481000000000012
Para el calculo del coeficiente de Pearson se realiza un procedimiento similar, se calcula con numpy.std la
desviacion estandar de X y Y y con ayuda del mismo for se realiza la siguiente formula: 
pearson += ((x[0]-xAverage)*(x[1]-yAverage)*(x[2]))/resultado
para lo que se obtiene un valor de 0.0033845918647466278.
Finalmente se calcula la funcion de densidad conjunta tridimensional con ayuda de ax.plot_trisurf y se
adjunta la imagen al repositorio, se hizo un gradiente de colores para que fuese mas facil de identificar.

