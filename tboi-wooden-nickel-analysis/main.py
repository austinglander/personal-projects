# YA01 LWVL - This seed grants 3 dimes, a nickel, and a penny within the first 5 uses of wooden nickel as the keeper
# This insane luck had me wondering just how lucky this really was, so here I am to find out
# I would love to use the actual game's RNG to discover seeds with similar or even greater luck, but that may be a bit above my paygrade
# For now, I will just do random trials

import matplotlib.pyplot as plt
import numpy as np


def wooden_nickel(n: int = 1) -> int:
    """ 
    Simulate n uses of wodden nickel and return the total value of pennies
    Odds are taken from the binding of isaac wiki: https://bindingofisaacrebirth.fandom.com/wiki/Wooden_Nickel
    Penny: 52%, Nickel: 6%, Dime: 1%, Nothing: 41% 
    """
    return sum(np.random.choice([0, 1, 5, 10], p=[0.41, 0.52, 0.06, 0.01], size=n))


# function to add value labels - https://www.geeksforgeeks.org/adding-value-labels-on-a-matplotlib-bar-chart/
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

# Run our simulations and collect the data
total_simulations = int(input("How many simulations to run?: "))
results_dict = {
    '0': 0,
    '1': 0,
    '5': 0,
    '10': 0
}
for i in range(total_simulations):
    results_dict[str(wooden_nickel())] += 1

# Setup our plot
x_vals = ['0', '1', '5', '10']
y_vals = [val / total_simulations for val in results_dict.values()]
plt.xlabel("Wooden Nickel Results")
plt.ylabel(f"Proportion of {total_simulations} simulations")
plt.bar(x_vals, y_vals)
addlabels(x_vals, y_vals)
plt.show()