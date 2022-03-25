# Taller sobre datos y ciclo de vida del aprendizaje automático

## Resumen

Cuando trabajamos en equipo con proyectos de aprendizaje automático la mejora de los resultados de nuestros experimentos implica sumergirnos en un ciclo de vida iterativo. En este proceso de repetición hay varios denominadores comunes, uno de ellos son los datos.

Los conjuntos de datos que usamos para nuestros experimentos no son estáticos, podemos añadir nuevas muestas o tomar las muestras agrupadas de forma diferente.
Para mantener la coherencia dentro de un equipo en estas iteraciones y saber con qué grupo de datos y con qué algoritmos se han obtenido cada uno de los resultados, necesitamos controlar estos procesos.

Pero, ¿hay alguna herramienta que nos ayude en esto?

## Objetivos

En este taller vamos a hacer girar el ciclo de vida del aprendizaje automático en torno el dato. Aprenderemos a hacer control de versiones de los datos y almacenaremos en remoto para trabajar de forma colaborativa.


## Qué vamos a hacer

## Código

En este repositorio trabajaremos con las herramientas 

### Estructura del proyecto

- prepare_data.py: Este fichero se encargará de leer los datos, normalizarlos y generar una partición de entrenamiento y otra de validación
- model.py: este fichero contiene el modelo en pytorch de una regresión lineal de las dimensiones que especifiquemos
- train_single.py, train_args.py y train.py: son el mismo fichero al que le vamos añadiendo mejoras. Lo he puesto en 3 para que podáis comparar facilmente. Se encarga de entrenar la red con los datos de entrenamiento, generar un modelo, graba las métricas y genera una imagen con la gráfica de pérdida.
- eval_single.py, eval_args.py y eval.py: son el mismo fichero mejorado. Lo he puesto en 3 para poder comparar de forma sencilla. Se encarga de tomar el modelo generado e introducir los datos de validación. La salida que producirá será el azul los valores de etiqueta y en rojo la predicción.
- dvc.yaml este fichero está vacío y hay que rellenarlo según el pipeline que ejecutéis con el contenido de single_run_dvc.yaml, single_run_dvc_args.yaml o loop_template_dvc.yaml. En cada caso reemplazáis el contenido de dvc.yaml con el contenido de cada uno de estos ficheros y estaría listo para ejecutar.

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

