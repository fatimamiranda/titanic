# titanic

Ejercicio 1 - Con el dataset de Titanic y pandas contesta a la siguientes preguntas o haz las siguientes tareas:
    Busca valores nulos de edad y sustituyelos por un valor que tenga sentido, explica por qué
    Existe alguna relación entre la supervivencia y la Clase del pasaje (primera, segunda y tercera clase)?
    Existe alguna relación entre la tasa de supervivencia y la edad?
    Como son de fuertes estas relaciones?
    Cuál es la personas más joven y más vieja que sobrevivieron?
    Cuál es la media de pago por billete del pasaje?
    Impacto del género en la supervivencia: ¿Cuál es la proporción de supervivencia entre hombres y mujeres? Pudo el género haber influido en las posibilidades de sobrevivir al desastre? Tip: df.groupby
    Con la letra de cabina, decide que hacer con los registros faltantes y busca las diferencias en la supervivencia. ¿Hubo localizacines de cabina que aunmentaron la posibilidad de sobrevivir? Tip: df['Cabin'].str[0] y groupby
    Sobrevivientes únicos y familias: Identifica si viajar solo o con familia afectó las tasas de supervivencia. Puedes crear una nueva columna que indique si el pasajero estaba solo o con familiares. Tip: crear nueva columna 'Solo' df['Solo'] = ((df['SibSp'] + df['Parch']) == 0).astype(int)
    Según lo anterior, pudo afectar a la supervivencia el viajas sólo o con familiares? Explica por qué.
    
