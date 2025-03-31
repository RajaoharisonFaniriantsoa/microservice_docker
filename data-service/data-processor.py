import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from sklearn.datasets import make_classification

load_dotenv()

# Générer des données synthétiques
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0)
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['label'] = y

# Se connecter à la base de données
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Créer la table si elle n'existe pas
cur.execute("""
    CREATE TABLE IF NOT EXISTS data_samples (
        id SERIAL PRIMARY KEY,
        feature1 FLOAT,
        feature2 FLOAT,
        label INT
    )
""")
conn.commit()

# Insérer les données
for _, row in df.iterrows():
    cur.execute(
        "INSERT INTO data_samples (feature1, feature2, label) VALUES (%s, %s, %s)",
        (row['feature1'], row['feature2'], row['label'])
    )
conn.commit()

# Calculer des statistiques
stats = df.describe().to_string()
print("Data Statistics:\n", stats)

cur.close()
conn.close()