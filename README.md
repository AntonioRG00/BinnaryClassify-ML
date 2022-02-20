# Temática del proyecto

**El proyecto consiste crear un modelo de aprendizaje que permita predecir si un cliente potencial se convertirá en un cliente real. El modelo se ha exportado a un archivo .pkl, que se usará para importarlo en una API REST hecha con Flask (project/FlaskApi.py) para así poder consultar por POST las predicciones de los nuevos clientes potenciales.**

El dataset se ha obtenido desde la página de Kaggle https://www.kaggle.com/ashydv/leads-dataset

Se ha usado clasificación binaria para el problema de predicción ya que la variable objetivo es la columna "Converted" que indica con 1 si el cliente se convierte en un cliente real y 0 en caso contrario.

# Librerias y planteamiento del proyecto

La librería principal que se ha usado para las predicciones es "Sklearn" junto a pandas y numpy para el tratamiento del dataset.

**Para el entrenamiento se ha usado un modelo supervisado de machine learning con "Logistic Regression" por ser un problema de clasificación binaria.**

**En las pruebas de validación se ha conseguido un 96% de aciertos**

Pasos que se han hecho para la construcción del modelo ML **(Se puede ver en ModelML.ipynb)**:

1. Preparación de los datos
2. Análisis de la importancia de las propiedades
3. Ingeniería de propiedades
4. Entrenamiento del modelo
5. Serialización del modelo

# Instalación y despliegue

**1. Una vez clonado el repositorio, en la raíz del proyecto lanzar "poetry install" para instalar las dependecias que requiere el proyecto.**
**2. Lanzar con python el archivo "FlaskApi.py" para levantar el microservicio (Hay que estar dentro del directorio project ya que usa rutas relativas).**

# Pesos de las columnas para la predicción

![imagen_pesos](https://user-images.githubusercontent.com/60214254/154853894-2c43392d-0df0-4c0c-b3cd-e60d43755cf2.png)

# Pruebas

**En los JSON de prueba solo se ha cambiado la columna "tags", ya que es la que más peso tiene en nuestra predicción**
Las pruebas se han hecho usando Postman. Se dejan aquí dos consultas de prueba: [ApiFlaskPostman.zip](https://github.com/AntonioRG00/BinnaryClassify-ML/files/8104418/ApiFlask.zip)

![ejemplo_cliente_real](https://user-images.githubusercontent.com/60214254/154853315-efbc3320-7e1c-4229-abe6-294744bae766.png)
![ejemplo_cliente_noreal](https://user-images.githubusercontent.com/60214254/154853561-b9fcc43a-f3db-4c09-9969-dedb594967a1.png)
