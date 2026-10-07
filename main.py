from ft_math import *

def main():

    arr = np.sort(np.array([12,1.2,2,3,4,5,5,45,24,15,10]))

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
