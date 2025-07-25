import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE


# 1. Cargar el dataset
df = pd.read_csv('titanic.csv')

# 2. Muestreo aleatorio simple (20%)
muestra_aleatoria = df.sample(frac=0.2, random_state=42)
print("Aleatorio:", muestra_aleatoria.shape)

# 3. Muestreo estratificado
_, muestra_estrat = train_test_split(
    df,
    test_size=0.2,
    stratify=df['Survived'],
    random_state=42
)
print("Estratificado:", muestra_estrat.shape)
print("Distribución original:", df['Survived'].value_counts(normalize=True).to_dict())
print("Estratificada:", muestra_estrat['Survived'].value_counts(normalize=True).to_dict())

# 4. SMOTE
X = df[['Age', 'Fare']].dropna()
y = df.loc[X.index, 'Survived']
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)
print("SMOTE:", pd.Series(y_res).value_counts().to_dict())

# 5. Guardar resultados
muestra_aleatoria.to_csv('titanic_muestra_aleatoria.csv', index=False)
muestra_estrat.to_csv('titanic_muestra_estratificada.csv', index=False)
pd.concat([X_res, y_res.rename('Survived')], axis=1).to_csv('titanic_smote.csv', index=False)


