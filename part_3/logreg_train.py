import pandas as pd
import numpy as np
import math

def predict( line, data):
    b = data[0]
    w = data[1:]

    z = b + np.dot(w, line)
    if z < -500:
        z = -500
    if z > 500:
        z = 500
    return 1 / (1 + math.exp(-z))

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
    n_values = (values - values.mean()) / values.std()

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
                w = w_norm / std
                b = b_norm - np.sum(w_orig * mean)

                # Assemblage [b, w1, w2, ..., wn] et écriture au format CSV
                line = np.concatenate(([b], w))
                f.write(",".join(map(str, line)) + "\n")
    except OSError:
        print("Cannot write trained.txt")
        exit()

if __name__ == '__main__':
    main()

