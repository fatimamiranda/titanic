#!/usr/bin/env python
# coding: utf-8
Ejercicio 1 - Con el dataset de Titanic y pandas contesta a la siguientes preguntas o haz las siguientes tareas:
Busca valores nulos de edad y sustituyelos por un valor que tenga sentido, explica por qué
# In[13]:


import pandas as pd
ruta_del_csv = 'titanic_dataset.csv'
dataset = pd.read_csv(ruta_del_csv)
#print(dataset.head())
print(dataset.info())
valores_nulos_edad = dataset['Age'].isnull()
print("Cantidad de valores nulos en la columna 'edad':", valores_nulos_edad.sum())
media_edad = dataset['Age'].mean()
print("Media edad: ",media_edad)
dataset['Age'].fillna(media_edad, inplace=True)
print(dataset.info())

Existe alguna relación entre la supervivencia y la Clase del pasaje (primera, segunda y tercera clase)?
# In[15]:


descripcion = dataset.groupby('Pclass')['Survived'].describe()
print(descripcion)


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de barras de supervivencia por clase
sns.countplot(x='Pclass', hue='Survived', data=dataset)
plt.show()

Existe alguna relación entre la tasa de supervivencia y la edad?
# In[18]:


descripcion_edad = dataset['Age'].describe()
print(descripcion_edad)


# In[19]:


sns.scatterplot(x='Age', y='Survived', data=dataset)
plt.show()


# In[21]:


from scipy.stats import pearsonr

correlacion, _ = pearsonr(dataset['Age'], dataset['Survived'])
print(f"Correlación entre edad y supervivencia: {correlacion}")


# In[ ]:




