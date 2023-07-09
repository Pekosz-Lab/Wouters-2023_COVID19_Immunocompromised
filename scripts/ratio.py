#!/usr/bin/env python

import argparse
import pandas as pd

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Divide values in a CSV or TXT file.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input CSV or TXT file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output TSV file')
args = parser.parse_args()

# Recognize file format based on extension 
file_extension = args.input.split('.')[-1].lower()

# Read the input file into a DataFrame based on the file format
if file_extension == 'csv':
    df = pd.read_csv(args.input)
elif file_extension == 'txt':
    df = pd.read_csv(args.input, delimiter='\t')
else:
    raise ValueError("Unsupported file format. Only CSV and TXT files are accepted.")

# Iterate over each cell in the DataFrame
for row in df.index:
    for col in df.columns:
        # Check if the column name is not "POS," "REF," "ALT," or "TYPE"
        if col not in ["POS", "REF", "ALT", "TYPE"]:
            # Check if the cell value is ".:."
            if str(df.at[row, col]) == ".:.":
                df.at[row, col] = 0
            else:
                # Check if the cell value contains two numbers separated by a colon
                if ':' in str(df.at[row, col]):
                    values = str(df.at[row, col]).split(':')

                    try:
                        # Perform division and replace the cell value with the result
                        result = float(values[1]) / float(values[0])
                        df.at[row, col] = result
                    except ZeroDivisionError:
                        # Handle division by zero error if necessary
                        df.at[row, col] = 'Error: Division by zero'

# Save the updated DataFrame to the output TSV file
df.to_csv(args.output, sep='\t', index=False)
print(f"Division completed. Result saved to '{args.output}'.")






