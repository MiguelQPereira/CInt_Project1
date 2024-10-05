import pandas as pd
import numpy as np
import simpful as sf
import argparse

from FIS.FuzzyInferenceSystem import fuzzy_system  # Import the fuzzy_system function

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
# ....

# Creates a DataFrame to store the results
results = pd.DataFrame(columns=["CLP_FIS", "CLP_NN"])


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
        "CLP_FIS": [result_fis],
        "CLP_NN": [result_fis]
    })

    # Concatenate the new data with the existing results DataFrame
    results = pd.concat([results, new_data], ignore_index=True)

# Save the results to a CSV file
results.to_csv(output_file, index=False)
print(f"Results saved to {output_file}")
