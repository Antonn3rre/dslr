import pandas as pd
import numpy as np
import math

def train( X, y):

    # m = nbe d'entree , n = nbe cours pour chaque entree
    m, n = X.shape

    b = 0.0
    w = np.zeros(n)

    learning_rate = 0.1
    iterations = 1000

    for i in range(iterations):
        z = b + np.dot(X, w) 

        z = np.clip(z, -500, 500)

        y_pred = 1 / (1 + np.exp(-z))

        error = y_pred - y
        # moyenne des erreurs (derivee du biais)
        db = (1 / m) * np.sum(error)
        # derivee des 13 cours
        dw = (1 / m)  * np.dot(X.T, error)

        b = b - learning_rate * db
        w = w - learning_rate * dw

    return b, w

def main():

    try:
        ds = pd.read_csv('../datasets/dataset_train.csv')
    except Exception:
        print("Error: cannot read dataset_train.csv")
        exit()

    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")
    if "Hogwarts House" in courses:
        courses.remove("Hogwarts House")

    # Retrieve values + Fill empty ones with mean
    values = ds[courses].fillna(ds[courses].mean()).to_numpy()

    # Normalisation
    # axis=0 permet de calculer colonne par colonne et pas tout ensemble
    n_values = (values - values.mean(axis=0)) / values.std(axis=0)

    houses = ["Ravenclaw", "Hufflepuff", "Slytherin", "Gryffindor"]
    y_raw = ds["Hogwarts House"].to_numpy()

    try:
        with open("trained.txt", "w") as f:
            for house in houses:
                # Binarisation : 1 si eleve est dans cette maison, 0 sinon
                y = np.where(y_raw == house, 1, 0)

                # Entrainement
                b_norm, w_norm = train(n_values, y)

                # Denormalisation
                w = w_norm / values.std(axis=0)
                b = b_norm - np.sum(w * values.mean(axis=0))

                # Assemblage [b, w1, w2, ..., wn] et écriture au format CSV
                line = np.concatenate(([b], w))
                f.write(",".join(map(str, line)) + "\n")
    except OSError:
        print("Cannot write trained.txt")
        exit()

if __name__ == '__main__':
    main()

