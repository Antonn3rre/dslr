import math
import pandas as pd
import matplotlib.pyplot as plt
import itertools

def main():
    """
    Display a scatter plot
    What are the two features that are similar?

    --> Display scatter plot comparing each courses between them
    """
    ds = pd.read_csv('datasets/dataset_train.csv')

    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")

    # Récupérer toutes les paires uniques (combinaisons de 2 colonnes)
    pairs = list(itertools.combinations(courses, 2))
    
    n_plots = len(pairs)
    fig, axes = plt.subplots(math.ceil(n_plots / 8), 8, figsize=(24, 36))
    axes = axes.flatten()

    for i, (course_a, course_b) in enumerate(pairs):
        ax = axes[i]
        ax.scatter(ds[course_a], ds[course_b], s=3, alpha=0.5, edgecolors='none')

        ax.set_title(f'{course_a} vs {course_b}', fontsize=7, pad=2)
        ax.set_xticks([])
        ax.set_yticks([])

    for j in range(n_plots, len(axes)):
        fig.delaxes(axes[j])

    plt.subplots_adjust(
        left=0.02, right=0.98, top=0.97, bottom=0.02, wspace=0.1, hspace=0.35
    )
    plt.show()

if __name__ == "__main__":
    main()

