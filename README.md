# Temática del proyecto

El proyecto consiste crear un modelo de aprendizaje que permita predecir si un cliente potencial se convertirá en un cliente real. El modelo se ha exportado a un archivo .pkl, que se usará para importarlo en una API REST hecha con Flask.

El dataset se ha obtenido desde la página de Kaggle https://www.kaggle.com/ashydv/leads-dataset

Se ha usado clasificación binaria para el problema de predicción ya que la variable objetido es la columna "Converted" que indica con 1 si el cliente se convierte en un cliente real y 0 en caso contrario.