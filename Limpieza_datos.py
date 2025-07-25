import pandas as pd
import numpy as np

# Cargar dataset
df = pd.read_csv("titanic.csv")

# 1. Perfilado rápido
print("Resumen general:")
print(df.info())
print("\nEstadísticas básicas:")
print(df.describe(include='all'))

# 2. Eliminar columnas irrelevantes
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# 3. Manejo de valores faltantes

# - Age: imputar con la mediana
df['Age'] = df['Age'].fillna(df['Age'].median())

# - Embarked: imputar con la moda
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# - Fare: en algunos datasets puede haber 1 valor nulo
if df['Fare'].isnull().sum() > 0:
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# 4. Estandarizar categorías de texto (por si hay inconsistencias)
df['Sex'] = df['Sex'].str.strip().str.lower()
df['Embarked'] = df['Embarked'].str.strip().str.upper()

# 5. Eliminar duplicados
df.drop_duplicates(inplace=True)

# 6. Outliers: detección por IQR para 'Fare' y 'Age'
def detectar_outliers(columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inf = Q1 - 1.5 * IQR
    limite_sup = Q3 + 1.5 * IQR
    outliers = df[(df[columna] < limite_inf) | (df[columna] > limite_sup)]
    print(f"\nOutliers en {columna}: {outliers.shape[0]} encontrados")
    return outliers

detectar_outliers('Fare')
detectar_outliers('Age')

# 7. Conversión de tipo de datos (por si acaso)
df['Pclass'] = df['Pclass'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
df['Sex'] = df['Sex'].astype('category')

# 8. Crear nuevas variables
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# 9. Mostrar primeras filas limpias
print("\nPrimeras filas tras limpieza:")
print(df.head())

# 10. Guardar dataset limpio
df.to_csv("titanic_limpio.csv", index=False)
print("\n Dataset limpio guardado como 'titanic_limpio.csv'")
