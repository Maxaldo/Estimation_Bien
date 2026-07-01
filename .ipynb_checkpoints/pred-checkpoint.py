import pandas as pd
import joblib


def ft_pred(type_bien, surface_m2, nb_pieces, nb_chambres, etage, dpe, code_postal):
    # Recharger ce que train.py a sauvegarde
    le_etage = joblib.load("utils/le_etage.joblib")
    le_type_bien = joblib.load("utils/le_type_bien.joblib")
    model = joblib.load("utils/model.joblib")
    mapping_dpe = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}

    # Construire une ligne avec les memes colonnes qu'a l'entrainement
    X = pd.DataFrame([{
        "type_bien": type_bien,
        "surface_m2": surface_m2,
        "nb_pieces": nb_pieces,
        "nb_chambres": nb_chambres,
        "etage": etage,
        "dpe": dpe,
        "code_postal": code_postal,
    }])

    # Meme encodage qu'a l'entrainement (transform, pas fit_transform)
    X["dpe"] = X["dpe"].map(mapping_dpe)
    X["etage"] = le_etage.transform(X["etage"])
    X["type_bien"] = le_type_bien.transform(X["type_bien"])
    X = X.fillna(-10000)
    X = X[model.feature_names_in_]

    return model.predict(X)[0]


print(ft_pred('Appartement à vendre', 50, 3, 2, '1 étages', "A", 75011.0))