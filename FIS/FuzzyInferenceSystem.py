import pandas as pd
import numpy as np
from FIS1 import FS_pt1
from FIS2 import FS_pt2

GENERATE = 0

# Load the CSV file into a DataFrame
data = pd.read_csv('CINTE24-25_Proj1_SampleData.csv')
output_data = []
errorsf = []
errors1 = []
errors2 = []
parameters = np.zeros(6)

###########################################################################################################
###########################################################################################################

def calculate_error(predicted, actual):
    return np.abs(predicted - actual)
    #return (predicted - actual) ** 2  # Squared error

###########################################################################################################
###########################################################################################################

def fuzzy_system (parameters):

    weight1 = 0.5
    weight2 = 0.5

    net_output = parameters[0]
    bandwidth = parameters[1]
    latency = parameters[2]
    cpu_load = parameters[3]
    mem_use = parameters[4]
    net_input= parameters[5]

    result1 = FS_pt1(net_output, bandwidth, latency)
    result2 = FS_pt2(cpu_load, mem_use, net_input)

    final_result = weight1 * result1['CLP'] + weight2 * result2['CLP']

    return final_result, result1['CLP'], result2['CLP']

###########################################################################################################
###########################################################################################################

def create_outcsv():

    return

###########################################################################################################
###########################################################################################################

for index, row in data.iterrows():
    parameters[0] = row['OutNetThroughput']
    parameters[1] = row['V_OutBandwidth']
    parameters[2] = row['Latency']
    parameters[3] = row['ProcessorLoad']
    parameters[4] = row['V_MemoryUsage']
    parameters[5] = row['InpNetThroughput']
    expected_clp = row['CLPVariation']
    
    # Perform inference (Sugeno inference here, can be different depending on your fuzzy system)
    predicted_clp, predicted_clp1, predicted_clp2 = fuzzy_system(parameters)

    # Calculate the error between predicted and actual output
    error = calculate_error(predicted_clp, expected_clp)
    errorsf.append(error)

    error = calculate_error(predicted_clp1, expected_clp)
    errors1.append(error)

    error = calculate_error(predicted_clp2, expected_clp)
    errors2.append(error)

    # Print or log the input and the corresponding error
    print(f"Row {index}: Predicted CLP = {predicted_clp}, Expected CLP = {expected_clp}, Error = {error}")
    # Append the row's data to the output list
    output_data.append({
        'Row': index,
        'OutNetThroughput': parameters[0],
        'V_OutBandwidth': parameters[1],
        'Latency': parameters[2],
        'ProcessorLoad': parameters[3],
        'V_MemoryUsage': parameters[4],
        'NetInput': parameters[5],
        'Expected_CLP': expected_clp,
        'Predicted_CLP': round(predicted_clp, 2),
        'FS_pt1_CLP': round(predicted_clp1, 2),
        'FS_pt2_CLP': round(predicted_clp2, 2),
        'Final_Error': round(errorsf[index], 2),
        'Partial_Error_FS1': round(errors1[index], 2),
        'Partial_Error_FS2': round(errors2[index], 2)
    })

# Create a DataFrame from the output data
output_df = pd.DataFrame(output_data)

# Save the DataFrame to a CSV file
output_df.to_csv('fuzzy_system_output.csv', index=False)

mean_f_error = np.mean(errorsf)
mean_error1 = np.mean(errors1)
mean_error2 = np.mean(errors2)

#mean_squared_error = np.sqrt(np.mean([error**2 for error in errors]))

print(f"Mean error across all inputs: final->{round(mean_f_error, 2)}, FS1->{round(mean_error1, 2)}, FS2->{round(mean_error2, 2)}")

if GENERATE == 1:
    gen_ds = []

    for i in range(15000):
        parameters[0] = round(np.random.rand(),2)
        parameters[1] = round(np.random.rand(),2)
        parameters[2] = round(np.random.rand(),2)
        parameters[3] = round(np.random.rand(),2)
        parameters[4] = round(np.random.rand(),2)
        parameters[5] = round(np.random.rand(),2)

        predicted_clp, predicted_clp1, predicted_clp2 = fuzzy_system(parameters)

        gen_ds.append({
            'OutNetThroughput': parameters[0],
            'V_OutBandwidth': parameters[1],
            'Latency': parameters[2],
            'ProcessorLoad': parameters[3],
            'V_MemoryUsage': parameters[4],
            'NetInput': parameters[5],
            'Expected_CLP': round(predicted_clp, 2)
        })

    data_set = pd.DataFrame(gen_ds)

    data_set.to_csv('generated_data_set.csv', index=False)