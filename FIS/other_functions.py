import simpful as sf
import matplotlib.pyplot as plt

def plot_membership_functions_individually(fuzzy_system, variable_name):
    """
    Plots each membership function of a linguistic variable in the fuzzy system individually.

    Parameters:
    fuzzy_system (sf.FuzzySystem): The fuzzy system containing the linguistic variable.
    variable_name (str): The name of the linguistic variable to plot.
    """
    print(fuzzy_system._variables.keys())

    # Get the linguistic variable
    linguistic_variable = fuzzy_system._variables[variable_name]

    # Iterate over each fuzzy set in the linguistic variable
    for term_name, fuzzy_set in linguistic_variable.sets.items():
        plt.figure()  # Create a new figure for each fuzzy set
        fuzzy_set.plot()  # Plot the fuzzy set
        plt.title(f'{term_name.capitalize()} Membership Function for {variable_name}')
        plt.xlabel(variable_name)
        plt.ylabel('Membership degree')

    # Show all the plots after plotting all fuzzy sets
    plt.show()