# Importaciones necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, mean_squared_error
from mlxtend.frequent_patterns import apriori, association_rules

# Cargar datos transformados
df = pd.read_csv("titanic_transformado.csv")

# Asegurar que no haya nulos
df.dropna(inplace=True)

# --- CLASIFICACIÓN: ¿Sobrevive o no? ---
X_clf = df.drop(columns=["Survived"])
y_clf = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("🔹 Clasificación - Random Forest")
print(classification_report(y_test, y_pred))

# --- REGRESIÓN: Predecir tarifa (Fare) ---
X_reg = df.drop(columns=["Fare", "Survived"])
y_reg = df["Fare"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg = LinearRegression()
reg.fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)

print("\n🔹 Regresión - Linear Regression")
print("MSE:", mean_squared_error(y_test_r, y_pred_r))

# --- AGRUPAMIENTO (CLUSTERING): KMeans con 3 clusters ---
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_clf)

print("\n🔹 Clustering - KMeans")
print(df["Cluster"].value_counts())

# --- REGLAS DE ASOCIACIÓN ---
# Convertir ciertas columnas a binario (solo para demostración)
df_assoc = df[["Sex_male", "Embarked_S", "Pclass", "Survived"]].copy()
df_assoc["Pclass"] = df_assoc["Pclass"].astype(str)
df_assoc = pd.get_dummies(df_assoc)

# Apriori para encontrar combinaciones frecuentes
frequent = apriori(df_assoc, min_support=0.1, use_colnames=True)
rules = association_rules(frequent, metric="lift", min_threshold=1.0)

print("\n🔹 Reglas de Asociación")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]].head())
