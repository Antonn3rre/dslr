from ft_math import *
import sys
import pandas as pd

def main():

    if (len(sys.argv) != 2):
        print('Error: wrong number of arguments')
        return

    ds = pd.read_csv(sys.argv[1])

    numeric_cols = ds.select_dtypes(include="number").columns.tolist()

    for col in numeric_cols:
        arr = np.sort(ds[col].to_numpy())

        print('Count:', ft_count(arr))
        meanValue = ft_mean(arr)
        print('Mean:', meanValue)
        print('Std:', ft_std(arr, meanValue))
        print('Min:', ft_min(arr))
        print('25%:', ft_quartile_25(arr))
        print('50%:', ft_quartile_50(arr))
        print('75%:', ft_quartile_75(arr))
        print('Max:', ft_max(arr))

    return

if __name__ == '__main__':
    main()
