#!/usr/bin/env python

import argparse

def extract_columns(input_file, output_file):
    # input vcf
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the column names
    header_index = 0
    for i, line in enumerate(lines):
        if not line.startswith('##'):
            header_index = i
            break

    # Extract column indices for "POS," "REF," "ALT," "INFO," and samples
    header = lines[header_index].strip().split('\t')
    try:
        pos_index = header.index("POS")
    except ValueError:
        print("'POS' column not found in the input file.")
        print("Available columns: ", header)
        return

    ref_index = header.index("REF")
    alt_index = header.index("ALT")
    format_index = header.index("FORMAT")
    info_index = header.index("INFO")
    sample_indices = [i for i, col in enumerate(header) if col != "POS" and col != "REF" and col != "ALT" and col != "INFO" and i > format_index]

    # Extract essential columns 
    output_lines = []
    output_lines.append('\t'.join(['POS', 'REF', 'ALT', 'TYPE'] + header[format_index+1:]))
    for line in lines[header_index + 1:]:
        columns = line.strip().split('\t')
        pos = columns[pos_index]
        ref = columns[ref_index]
        alt = columns[alt_index]
        info = columns[info_index]
        type_value = ""
        for info_item in info.split(';'):
            if info_item.startswith("TYPE="):
                type_value = info_item.split('=')[1]
                break
        samples = [columns[i].replace(',', '') for i in sample_indices]  # Remove commas
        extracted_columns = [pos, ref, alt, type_value] + samples
        output_lines.append('\t'.join(extracted_columns))

    # Write the extracted columns to the output file
    with open(output_file, 'w') as file:
        file.write('\n'.join(output_lines))

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract specific columns from a text file.')
    parser.add_argument('-i', '--input_file', help='path to the input file', required=True)
    parser.add_argument('-o', '--output_file', help='path to the output file', required=True)
    args = parser.parse_args()

    # Extract columns and write to the output file
    extract_columns(args.input_file, args.output_file)
