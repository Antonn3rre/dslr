import csv
import numpy as np

# theta0 = ordonnee a l'origine
# theta1 = pente

#TODO   check normalisation

def gradient(m, n_mileage, n_price):

    theta0 = 0
    theta1 = 0

    learning_rate = 0.1
    iterations = 100


    for _ in range(iterations):

        estimated_price = theta0 + theta1 * n_mileage
        tmp_theta0 = learning_rate * (1/m) * np.sum( estimated_price  - n_price)
        tmp_theta1 = learning_rate * (1/m) * np.sum( (estimated_price - n_price ) * n_mileage)

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    return theta0, theta1
    



def main():

    # Parse file
    try:
        data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)
    except:
        print("Error: can't retrieve data.csv values")
        return

    mileage = data[:,0]
    price = data[:,1]
    m = len(mileage)

    # Normalize values
    n_price = ( price - price.mean() ) / price.std()
    n_mileage = (mileage - mileage.mean()) / mileage.std()

    # Training (descente de gradient)
    theta0, theta1 = gradient(m, n_mileage, n_price)

    theta1_original = theta1 * price.std() / mileage.std()

    # Re scale values
    theta0_original = (
        theta0 * price.std()
        + price.mean()
        - theta1_original * mileage.mean()
    )

    with open("thetas.txt", "w") as f:
        f.write(f"{str(theta0_original)}\n")
        f.write(f"{str(theta1_original)}\n")

    print(theta0_original, theta1_original)

    return
    

if __name__ == '__main__':
    main()
