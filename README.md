# Taller sobre datos y ciclo de vida del aprendizaje automático

## Resumen

Cuando trabajamos proyectos de aprendizaje automático en equipo, la mejora de los resultados de nuestros experimentos implica sumergirnos en un ciclo de vida iterativo. En este proceso de repetición hay varios denominadores comunes, uno de ellos es el conjunto de datos.

El conjunto de datos que usamos para nuestros experimentos no es estáticos, podemos añadir nuevas muestas o tomar las muestras agrupadas de forma diferente. Para mantener la coherencia, dentro de un equipo en estas iteraciones y saber con qué grupo de datos y con qué algoritmos se han obtenido cada uno de los resultados, necesitamos controlar estos procesos.

Pero, ¿hay alguna herramienta que nos ayude en esto?

## Objetivos

En este taller vamos a hacer profundizar en el ciclo de vida del aprendizaje automático en torno al dato. Aprenderemos a hacer control de versiones y  almacenaremos los datos en remoto para trabajar de forma colaborativa. Para ellos usaremos la herramienta [Dvc](https://dvc.org/). Dvc es el acronimo de data versioning control. Esta herramienta trabaja junto con Git para permitir versionar nuestros datos junto con nuestro código. La principal ventanja de poder ligar datos e implementación es que podemos tener ramas que tengan el código y los datos con los entrenamos el modelo juntos.

### Qué vamos a hacer

El problema que vamos a tratar es algo sencillo. Es pasar de Celsius a Farenheit, tiene una fórmula matemática pero vamos a hacer una regresión lineal. Como véis, no queremos enredarnos en un problema muy complejo. No vamos a poner a prueba nuestra habilidad para generar modelos complejos. Queremos entender y practicar en el ciclo de vida del aprendizaje automático y los datos. En resumen, entender y ganar experiencia con estos problemas.

## 3 Requisitos previos

1. Crearemos un entorno virtual (descrito más alante) que contendrá las dependencias necesarias para el taller.
2. Crearemos un directorio nuevo en Google Drive y obtendremos su enlace para compartirlo con dvc. Es importante dar permisos a directorio para que cualquiera pueda acceder al directorio si tiene el enlace. De no ser así no DVC no podrá acceder para poner lo dato allí.
3. Vamos a crear **5 directorios** vacíos: _data, evaluations, metrics, models, partitions_.

    1. En _data_ vamos a poner nuestro fichero _training.csv_ con los datos de nuestro problema.
    2. Pondremos en _evaluations_ la gráfica de evaluación que hemos obtenido de testear nuestro algoritmo.
    3. _metrics_ nos servirá para guardar las métricas de entrenamiento.
    4. En _models_ depositaremos los modelos entrenados.
    5. Finalmente en _partitions_ guardaremos los datos trabajados para entrenar.

## Estructura de trabajo

Antes de entrar en el código, vamos a dar un primer paso entendiendo la estructura que montaremos para el proyecto

1. Preparación de datos. Tomaremos los datos y generaremos un fichero de metadatos que nos van ayudar para entrenar mejor.
2. Entrenamiento de modelos. Con los datos de las particiones, para entrenar nuestro algoritmo, generamos un modelo de regresión lineal en pytorch.
3. Cálculo de métricas. A medida que entrenamos vamos extrayendo las métricas más representativas.
4. Evaluación del modelo. Finalmente evaluamos nuestro modelo con un conjunto de datos.

### El código

- _prepare_data.py_: Este fichero se encargará de leer los datos, normalizarlos y generar una partición de entrenamiento y otra de validación

- _model.py_: este fichero contiene el modelo en pytorch de una regresión lineal de las dimensiones que especifiquemos

- _train_single.py_, train_args.py y train.py: son el mismo fichero al que le vamos añadiendo mejoras. Lo he puesto en 3 para que podáis comparar facilmente. Se encarga de entrenar la red con los datos de entrenamiento, generar un modelo, graba las métricas y genera una imagen con la gráfica de pérdida.

- _eval_single.py_, eval_args.py y eval.py: son el mismo fichero mejorado. Lo he puesto en 3 para poder comparar de forma sencilla. Se encarga de tomar el modelo generado e introducir los datos de validación. La salida que producirá será el azul los valores de etiqueta y en rojo la predicción.

- _dvc.yaml_ este fichero está vacío y hay que rellenarlo según el pipeline que ejecutéis con el contenido de single_run_dvc.yaml, single_run_dvc_args.yaml o loop_template_dvc.yaml. En cada caso reemplazáis el contenido de dvc.yaml con el contenido de cada uno de estos ficheros y estaría listo para ejecutar.

Os recomiendo clonar el repositorio es vuestras máquinas y a partir de aquí hacer el taller en un directorio diferente.

### Configuración del entorno virtual

Pasos a seguir:

1. Creamos en Anaconda Navigator un nuevo entorno virtual.
2. Instalamos las dependencias y paquetes siguientes: pandas, numpy, pytorch, sklearn, matplotlib
3. Abriremos un terminal desde el entorno virtual creado en anaconda y instalaremos los paquetes de dvc porque posiblemente no estarán listados dentro de Anaconda

    ```python
    pip install dvc
    pip install "dvc[gdrive]"
    ```

>Para continuar tenemos que tener el entorno virtual con lo anteriormente detallado. En vuestro caso con conda activo para el directorio de trabajo en Visual Studio sería lo más sencillo.

### Inicialización

1. Abrimos Visual Studio Code y copiamos los ficheros como hemos sugerido
2. Guardaremos en el proyecto en una capeta que podamos localizar despues desde el terminal de Anaconda Navigator
3. Abrimos una nueva ventana en el terminal desde anaconda navigator
4. Seguimos con los siguientes comandos

    ```python
    git init
    dvc init
    dvc add data
    dvc remote add --default myremote gdrive://<ID_CARPETA_DE_GOOGLE_DRIVE> # Este es el id del final de la url al dar a compartir dentro de google drive
    dvc push data # ahora debería dejarnos subir nuestros datos a google drive
    ```

### Ejecutamos los pipelines

 Una vez que tenemos los datos y los ficheros creados necesitaremos crear las carpetas: partitions, metrics, models y evaluations.

```python
dvc dag
dvc repro
```

> Una vez probados las ficherso cambiaremos los datos añadiendo una nueva columan al csv y volveremos a ejecutar

```python
dvc repro
```

Se volverán a ejecutar todos los pasos de nuestro pipeline.
Recordemos que solo mantenemos de forma manual el directorio data. Todos los demás datos se subirán solos cuando hagamos 

```python
dvc push
```

