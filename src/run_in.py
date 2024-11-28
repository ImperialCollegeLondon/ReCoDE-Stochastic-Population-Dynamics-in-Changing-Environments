import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    # Initialize lists to store regression coefficients and intercepts
    coef_lst = []
    int_lst = []

    def run():
        """
        Executes 1000 simulation runs of the cell division process.
        For each run:
        - Performs linear regression on sorted division times vs. log(N-1).
        - Saves the regression coefficient and intercept for analysis.
        """
        for _ in range(1000):  # Perform 1000 runs
            # Run the cell division simulation
            time_independent_results = time_independent_main()

            # Extract and sort division times from the results
            time_independent_all_division_time = np.sort(np.array(time_independent_results)[:, 2])

            # Define the number of samples for regression
            num = 300
            conn = {
                "log N-1": np.log(np.arange(num) + 1),  # Logarithm of rank (log(N-1))
                "time": time_independent_all_division_time[:num],  # Corresponding division times
            }

            # Prepare data for linear regression
            xdata = conn["log N-1"].reshape(-1, 1)  # Reshape to 2D array for sklearn
            ydata = conn["time"]

            # Fit a linear regression model
            regr = LinearRegression()
            regr.fit(xdata, ydata)

            # Save the coefficient and intercept
            coef_lst.append(regr.coef_[0])  # Regression slope (coefficient)
            int_lst.append(regr.intercept_)  # Regression intercept

    # Run the simulation and regression analysis
    run()

    # Create a DataFrame from the results
    data = pd.DataFrame({'coef': coef_lst, 'interception': int_lst})

    # Save the results to a compressed NumPy file
    np.savez_compressed('data_independ.npz', coef=np.array(coef_lst), intercept=np.array(int_lst))

    # Plotting placeholder (expand as needed)
    plt.hist(coef_lst, bins=30, alpha=0.7, label='Coefficients')
    plt.xlabel('Coefficient')
    plt.ylabel('Frequency')
    plt.legend()
    plt.title('Distribution of Regression Coefficients')
    plt.show()
