import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import joblib


def ft_train():
    os.makedirs("utils", exist_ok=True)
    data = pd.read_csv("data.csv")
    data = data[data["prix_eur"] < 5000000]
    X = data.drop(columns=["Unnamed: 0", "prix_eur", "prix_m2", "url", "latitude", "longitude", "adresse"])
    y = data["prix_eur"]

    mapping_dpe = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}
    X["dpe"] = X["dpe"].map(mapping_dpe)

    le_etage = LabelEncoder()
    X["etage"] = le_etage.fit_transform(X["etage"])
    joblib.dump(le_etage, "utils/le_etage.joblib")

    le_type_bien = LabelEncoder()
    X["type_bien"] = le_type_bien.fit_transform(X["type_bien"])
    joblib.dump(le_type_bien, "utils/le_type_bien.joblib")

    X = X.fillna(-10000)

    model = GradientBoostingRegressor(n_estimators=300, learning_rate=0.01,
                                      max_depth=5, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "utils/model.joblib")


ft_train()