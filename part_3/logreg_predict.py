import pandas as pd
import numpy as np

def predict( line, data):
    return 2

def main():

    ds = pd.read_csv('../datasets/dataset_test.csv')
    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")
    if "Hogwarts House" in courses:
        courses.remove("Hogwarts House")

    # Fill empty values with mean

#todo

    # Open prediction file
    try:
        data = np.loadtxt("trained.txt", delimiter=",")
    except (OSError, ValueError) as e:
        # Print error and leave
        print("Error :/")
        exit()

    values = ds[courses].fillna(ds[courses].mean()).to_numpy()


    with open("houses.csv", "w") as f:
        f.write("Index,Hogwarts House\n")
        for index, line in enumerate(values):
            ravenclaw = [predict(line, data[0]), "Ravenclaw"]
            hufflepuff = [predict(line, data[1]), "Hufflepuff"]
            slytherin = [predict(line, data[2]), "Slytherin"]
            gryffindor = [predict(line, data[3]), "Gryffindor"]

            winner = max(ravenclaw, hufflepuff,slytherin, gryffindor)
            f.write(f"{index},{winner[1]}")

if __name__ == '__main__':
    main()

