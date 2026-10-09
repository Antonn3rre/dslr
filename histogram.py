import sys
import math
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
        Display a histogram
        Which Hogwarts course has a homogenous score distribution between all four houses

        --> Display score for each house in all courses
    """

    ds = pd.read_csv('datasets/dataset_train.csv')
    courses = ds.select_dtypes(include="number").columns.tolist()
    
    if "Index" in courses:
        courses.remove("Index")

    # Only courses and house names
    house_col_name = 'Hogwarts House'
    tg_cols = [house_col_name] + courses
    filtered_ds = ds[tg_cols]
    houses = ds[house_col_name].dropna().unique()
    print('Houses:', houses)
    print('Courses:',  courses)
    
    # Create empty subplots fig
    n_courses = len(courses)
    fig, axes = plt.subplots(math.ceil(n_courses / 4), 4)
    axes = axes.flatten()  # Transforme la matrice 2D d'axes en liste 1D

    # Iterate over all courses
    for i, course in enumerate(courses):
        ax = axes[i]
        for house in houses:
            data = ds[ds[house_col_name] == house][course].dropna()
            
            ax.hist(data, alpha=0.5, label=house)
        
        ax.set_title(course, fontsize=10)
        ax.tick_params(labelsize=8)

    # Nettoyage des sous-graphes vides (cases 14, 15 et 16)
    for j in range(n_courses, len(axes)):
        fig.delaxes(axes[j])

    # 5. Légende globale et ajustement de l'espacement
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right", fontsize=11)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
