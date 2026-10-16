###############################################################
### to avoid unnecessary conflicts or a copy paste of the plot script, the 3 parts
# will be merged. The file cnv_data.csv have to be given as an input

# required to create a dataframe
import pandas as pd
# Required to recover the file name as an input, to avoid to hardcode it
import argparse
# Require to read a csv file
import csv
# Required to create the plot
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Read the cnv_data.csv file to make some plot with it")
parser.add_argument('file', help="Choose the csv file")
input = parser.parse_args()

# Now i have my dataframe
#csv_file = pd.read_csv(input)

with open(input.file, "r", newline ='', encoding='latin-1') as file:
    reader = csv.reader(file, delimiter = ",")
    # create a variable that recover all of the data
    data = list(reader)

df = pd.DataFrame(data)

# Print the name of the column to be used later
print(df.columns.tolist())

# I want to use the second and third columns as values. Convert it into numerics
for col in df.columns[1:3]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#print(df)

# remove the first row, that included strings
clear_df = df.dropna() 
#print(clear_df)

### Create the plot
# First, create the base, with the axis
plt.figure(figsize=(8, 6))
# Set the x and y values, and a color for the points
plt.scatter(clear_df[1], clear_df[2], color='blue')
plt.title("Ration log2 depending on the position")
plt.xlabel("position (mb)")
plt.ylabel("Ratio (log2)")
# Save the figure
plt.savefig("plot_part_3.png", dpi=150, bbox_inches="tight")



