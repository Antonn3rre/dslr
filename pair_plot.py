import math
import pandas as pd
import matplotlib.pyplot as plt
import itertools

def main():
    """
    Display a pair plot

    Intersection between the same course diplay its histogram
    """
    ds = pd.read_csv('datasets/dataset_train.csv')

    courses = ds.select_dtypes(include="number").columns.tolist()

    if "Index" in courses:
        courses.remove("Index")
   
    n_courses = len(courses) 
    fig, axes = plt.subplots(n_courses, n_courses, figsize=(24, 36))

    for i, course_a in enumerate(courses):
        
        for j, course_b in enumerate(courses):

            if ( i == j ):
                #diplay_histogram()
                pass
            else:
                # Display scatter plot
                axes[i][j].scatter(ds[course_a], ds[course_b], s=3, alpha=0.5, edgecolors='none')
                axes[i][j].set_xticks([])
                axes[i][j].set_yticks([])
    
    plt.subplots_adjust(
        left=0.02, right=0.98, top=0.97, bottom=0.02, wspace=0.1, hspace=0.35
    )
    plt.show()

if __name__ == "__main__":
    main()
