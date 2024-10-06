import joblib
import pandas as pd
import numpy as np
import simpful as sf
import argparse
from sklearn.metrics import mean_squared_error, mean_absolute_error

from FIS.FuzzyInferenceSystem import fuzzy_system  # Import the fuzzy_system function

##############################################################################################
##############################################################################################

def map_to_class(y_pred):
    if y_pred <= -0.15:
        return 'Decrease'
    elif y_pred >= 0.15:
        return 'Increase'
    else:
        return 'Maintain'

##############################################################################################
##############################################################################################

# Create the argument parser
parser = argparse.ArgumentParser(description="TestMe script to process a CSV file")

# Add a positional argument for the input file, with default='Proj1_TestS.csv'
parser.add_argument(
    'input', 
    nargs='?',   # '?' makes the argument optional
    default='Proj1_TestS.csv',  # Default value if no argument is passed
    help="Path to the input CSV file (default is 'Proj1_TestS.csv')"
)

# Parse the arguments
args = parser.parse_args()

# Access the input argument
input_file = args.input


output_file = 'TestResult.csv'

# Puts Input CSV file into a DataFrame
data = pd.read_csv(input_file)

# Load the pre-trained neural network model
mlp = joblib.load('NN/mlp_model.pkl')


# Creates a DataFrame to store the results
results = pd.DataFrame(columns=["FIS", "NNRegressor", "NNClassifier", "Mean Absolute Error", "Mean Squared Error"])

x = data.drop(columns=['CLPVariation', 'V_Latency', 'V_OutNetThroughput', 'V_InpNetThroughput', 'V_ProcessorLoad', 'MemoryUsage', 'OutBandwidth'],)
x = x[['OutNetThroughput', 'V_OutBandwidth', 'Latency', 'ProcessorLoad', 'V_MemoryUsage', 'InpNetThroughput']]
y = data['CLPVariation']

y_pred = mlp.predict(x)

for index, row in data.iterrows():
    # Get the parameters for FIS
    parameters = np.array([row['OutNetThroughput'], row['V_OutBandwidth'], row['Latency'], 
                            row['ProcessorLoad'], row['V_MemoryUsage'], row['InpNetThroughput']])
    
    # Predict using the fuzzy system
    result_fis, _, _ = fuzzy_system(parameters)  # Assuming fuzzy_system() combines FS_pt1 and FS_pt2
    
    # Predict using the neural network
    # ....

    # Append the results to the DataFrame
    new_data = pd.DataFrame({
        "FIS": [result_fis],
        "NNRegressor": [y_pred[index]],
        "NNClassifier": [map_to_class(y_pred[index])]
    })

    # Concatenate the new data with the existing results DataFrame
    results = pd.concat([results, new_data], ignore_index=True)

# Save the results to a CSV file
results.loc[0, "Mean Absolute Error"] = mean_absolute_error(y, y_pred)
results.loc[0, "Mean Squared Error"] = mean_squared_error(y, y_pred)
results.to_csv(output_file, index=False)
print(f"Results saved to {output_file}")
