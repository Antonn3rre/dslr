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
        ds = pd.read_csv('../datasets/dataset_test.csv')
    except Exception:
        print("Error: cannot read dataset_test.csv")
        exit()

    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")
    if "Hogwarts House" in courses:
        courses.remove("Hogwarts House")


#todo

    # Open prediction file
    try:
        data = np.loadtxt("trained.txt", delimiter=",")
    except (OSError, ValueError) as e:
        # Print error and leave
        print("Error :/")
        exit()

    if data.ndim != 2 or data.shape[0] != 4 or data.shape[1] != len(courses) + 1:
        print("Error: invalid weights format in trained.txt")
        exit()

    # Retrieve values + Fill empty ones with mean
    values = ds[courses].fillna(ds[courses].mean()).to_numpy()

    try:
        with open("houses.csv", "w") as f:
            f.write("Index,Hogwarts House\n")
            for index, line in enumerate(values):
                ravenclaw = [predict(line, data[0]), "Ravenclaw"]
                hufflepuff = [predict(line, data[1]), "Hufflepuff"]
                slytherin = [predict(line, data[2]), "Slytherin"]
                gryffindor = [predict(line, data[3]), "Gryffindor"]
    
                winner = max(ravenclaw, hufflepuff,slytherin, gryffindor)
                f.write(f"{index},{winner[1]}\n")
    except OSError:
        print("Cannot write houses.csv")
        exit()

if __name__ == '__main__':
    main()

