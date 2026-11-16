import math
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import textwrap

def main():
    """
    Display a pair plot

    Intersection between the same course diplay its histogram
    """
    ds = pd.read_csv('datasets/dataset_train.csv')

    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")
   
    house_col_name = 'Hogwarts House'
    houses = ds[house_col_name].dropna().unique()
    n_courses = len(courses) 
    fig, axes = plt.subplots(n_courses, n_courses, figsize=(24, 36))

    for i, course_a in enumerate(courses):
        
        for j, course_b in enumerate(courses):

            if ( i == j ):
                #diplay_histogram()
                for house in houses:
                    data = ds[ds[house_col_name] == house][course_a].dropna()
                    axes[i][j].hist(data, alpha=0.5, label=house)

            else:
                # Display scatter plot
                axes[i][j].scatter(ds[course_a], ds[course_b], s=3, alpha=0.5, edgecolors='none')
            axes[i][j].set_xticks([])
            axes[i][j].set_yticks([])
            if i == 0:
                axes[i][j].set_title(textwrap.fill(course_b, 15), fontsize=9, pad=8)

            if j == 0:
                axes[i][j].set_ylabel(
                    textwrap.fill(course_a, 15),
                    fontsize=9,
                    rotation=0,
                    ha="right",
                    va="center",
                    labelpad=10,
                )
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper right", bbox_to_anchor=(0.98, 0.98), title="Houses")

    plt.tight_layout()
    plt.subplots_adjust(
        left=0.08, right=0.88, top=0.92, bottom=0.02, wspace=0.1, hspace=0.35
    )
    plt.show()

if __name__ == "__main__":
    main()
