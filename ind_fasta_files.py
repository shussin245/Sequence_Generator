# -*- coding: utf-8 -*-
"""ind_fasta_files.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pE2L8dZQaYnBB5RwS1vXv08d06NK9zFb
"""

# Define the input FASTA file and an output directory
input_fasta_file = '/content/ref_w_strains.fasta'
output_directory = '/content/FASTA_Files/'

# Create the output directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)

# Initialize variables to keep track of the current sequence name and content
current_sequence_name = None
current_sequence_content = []

# Read the input FASTA file
with open(input_fasta_file, 'r') as fasta_file:
    for line in fasta_file:
        line = line.strip()
        if line.startswith('>'):
            # This line is a sequence header
            if current_sequence_name:
                # Write the previous sequence to a new FASTA file
                output_file_name = os.path.join(output_directory, current_sequence_name[1:] + '.fa')
                with open(output_file_name, 'w') as output_file:
                    output_file.write(current_sequence_name)
                    output_file.write('\n')
                    output_file.write('\n'.join(current_sequence_content))
                current_sequence_content = []  # Clear the content
            current_sequence_name = line
        else:
            # This line is part of the sequence
            current_sequence_content.append(line)

# Write the last sequence to a new FASTA file
if current_sequence_name:
    output_file_name = os.path.join(output_directory, current_sequence_name[1:] + '.fa')
    with open(output_file_name, 'w') as output_file:
        output_file.write(current_sequence_name)
        output_file.write('\n')
        output_file.write('\n'.join(current_sequence_content))

print('FASTA sequences have been split into individual files.')

# Download the file
from google.colab import files
files.download("/content/FASTA_Files/")