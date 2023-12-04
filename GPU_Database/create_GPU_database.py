import pandas as pd

# Import data from the 4 sheets in the excel dump
high_end = pd.read_excel("GPU_database.xlsx", "High End", header=None)
high_mid_range = pd.read_excel("GPU_database.xlsx", "High Mid Range", header=None)
low_mid_range = pd.read_excel("GPU_database.xlsx", "Low Mid Range", header=None)
low_end = pd.read_excel("GPU_database.xlsx", "Low End", header=None)

# Combine into one pandas dataframe
df = pd.concat([high_end, high_mid_range, low_mid_range, low_end])

# Create a list to store organized data
organized = []

# Iterate over the data
for i in range(0, len(df), 3):
    gpu_name = df.iloc[i, 0]
    performance = int(df.iloc[i+2, 0].split(" ")[0].replace(',', ''))
    if df.iloc[i+2, 0].split(" ")[1] != 'NA':
        price = float(df.iloc[i+2, 0].split(" ")[1].replace(',', '').replace('*', ''))
    else:
        price = 0 # Maybe this should be None
    organized.append([gpu_name, performance,  price])

# print(organized[:5])

organized_df = pd.DataFrame(organized)
     
# Save the dataframe to csv
organized_df.to_csv('organized_GPU_database.csv', index=False, header=["GPU", "Score", "Price"])