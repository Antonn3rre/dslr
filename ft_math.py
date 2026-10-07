import numpy as np
import math

def ft_count(arr: np.array) -> float:
    mydict = dict(zip(arr,arr))
    return len(mydict)

def ft_mean(arr: np.array) -> float:
    return np.sum(arr) / len(arr)

def ft_std(arr: np.array, meanValue: float) -> float:
    """
        describes how much variation or dispersion there is in a set of data points
        Step 1: Calculate the mean (in args)
        Step 2: Calculate squared differences of data values from the mean
        Step 3 (Variance): Calculare average of squared differences
        Step 4: Calculate the square root of variance
    """
    step2 = np.array(pow(arr - meanValue, 2))
    variance = ft_mean(step2)
    stdValue = math.sqrt(variance)
    return stdValue

def ft_min(arr: np.array) -> float:
    return arr[0]

def ft_max(arr: np.array) -> float:
    return arr[len(arr) - 1]

def ft_quartile_25(arr: np.array) -> float:
    return arr[round((len(arr) + 1) / 4)]

def ft_quartile_50(arr: np.array) -> float:
    return arr[round((len(arr) + 1) / 2)]

def ft_quartile_75(arr: np.array) -> float:
    return arr[round(3 * (len(arr) + 1) / 4)]


