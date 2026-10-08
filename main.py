from ft_math import *
import sys
import pandas as pd

def main():

    if (len(sys.argv) != 2):
        print('Error: wrong number of arguments')
        return

    ds = pd.read_csv(sys.argv[1])

    numeric_cols = ds.select_dtypes(include="number").columns.tolist()

    header = (
        f"{'Column name':<32} | {'Count':>10} | {'Mean':>12} | {'Std':>12} | "
        f"{'Min':>12} | {'25%':>12} | {'50%':>12} | {'75%':>12} | {'Max':>12}"
    )
    print(header)
    print("-" * len(header))

    for col in numeric_cols:
        arr = ds[col].dropna().to_numpy()
        arr = np.sort(arr)

        col_count = ft_count(arr)
        col_mean = ft_mean(arr)
        col_std = ft_std(arr, col_mean)
        col_min = ft_min(arr)
        col_quart_25 = ft_quartile_25(arr)
        col_quart_50 = ft_quartile_50(arr)
        col_quart_75 = ft_quartile_75(arr)
        col_max = ft_max(arr)

        print(
            f"{col:<32} | "
            f"{col_count:>10.0f} | "
            f"{col_mean:>12.2f} | "
            f"{col_std:>12.2f} | "
            f"{col_min:>12.2f} | "
            f"{col_quart_25:>12.2f} | "
            f"{col_quart_50:>12.2f} | "
            f"{col_quart_75:>12.2f} | "
            f"{col_max:>12.2f}"
        )

    """
        print('Count:', ft_count(arr))
        meanValue = ft_mean(arr)
        print('Mean:', meanValue)
        print('Std:', ft_std(arr, meanValue))
        print('Min:', ft_min(arr))
        print('25%:', ft_quartile_25(arr))
        print('50%:', ft_quartile_50(arr))
        print('75%:', ft_quartile_75(arr))
        print('Max:', ft_max(arr))
    """
    return

if __name__ == '__main__':
    main()
