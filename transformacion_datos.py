import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer


# Cargar el dataset
df = pd.read_csv("titanic.csv")

# --- Variables categóricas y numéricas ---
cat_features = ['Sex', 'Embarked', 'Pclass']
num_features = ['Fare', 'Age']

# --- Pipelines de transformación ---
# Categóricas: imputar y OneHotEncoding
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
])

# Numéricas: imputar y escalar (más log-transformación para Age)
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('log_transform', FunctionTransformer(lambda x: np.log1p(x), feature_names_out='one-to-one')),
    ('scaler', StandardScaler())
])

# Unir todo
preprocessor = ColumnTransformer([
    ('cat', cat_pipeline, cat_features),
    ('num', num_pipeline, num_features)
])

# Aplicar transformaciones
X_transformed = preprocessor.fit_transform(df)

# Convertir a DataFrame
columns_transformed = preprocessor.get_feature_names_out()
df_transformed = pd.DataFrame(X_transformed, columns=columns_transformed)

# Mostrar y guardar
print(df_transformed.head())
df_transformed.to_csv("titanic_transformado.csv", index=False)
