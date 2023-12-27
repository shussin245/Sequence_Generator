# -*- coding: utf-8 -*-
"""CAMISIM_Config_Files

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h5akterqVm41UeCYe9C7hitxVv0AwOJ0

Libraries
"""

import string
import random
import numpy as np
import math
import csv

"""Creating Sequence Names"""

random.seed(100442971)
pct_ids = [50, 80, 90, 95, 96, 97, 98, 99, 99.5, 99.9]
n_strains = [0, 1, 2, 3, 4, 5, 10, 15, 20, 50]
depths = [3, 5, 10, 15, 20, 25, 50, 75, 100, 200]

pct_id_labels = [str(x) + "%ID" for x in pct_ids]
pct_id_dict = dict(zip(pct_ids, pct_id_labels))

n_strain_labels = [str(y) + "STR" for y in n_strains]
n_strain_dict = dict(zip(n_strains, n_strain_labels))

depth_labels = [str(z) + "DPT" for z in depths]
depth_dict = dict(zip(depths, depth_labels))

#print(pct_id_dict)
#print(n_strain_dict)
#print(depth_dict)

str_names = []
vec_names = []

for a in pct_ids:
  for b in n_strains:
    for c in depths:

      vec_name_list = [a,b,c]
      vec_name = np.array(vec_name_list)
      str_name = f"{pct_id_dict[a]}_{n_strain_dict[b]}_{depth_dict[c]}"
      str_names.append(str_name)
      vec_names.append(vec_name)
      #print(str_name)
      #print(vec_name)

#print(len(sequences))
#print(len(names))
#print(names[0][0][0])
#names_set = set(names)
#print(len(names_set))

"""Generating Configuration Files for CAMISIM

1. Create a for-loop that goes through each of the names in the names list
2. Obtain the # of strains from each name
3. For each name, the number of additional strains will be generated and will be numberered according to the strain number
4. Each strain will be at the same %id, but the # of same bases should be changed accordingly (a lower %id will yield more bases to be changed)
5. A dictionary should be created to add all the additional strains + the reference sequence associated with the strains together
6. Create a metadata and id to genome file (in .tsv format) for each ref+strain set
"""

random.seed(100442971)
lens = []

for n in range(0, 1000):
  paths = []
  genomes = []
  genomes.append(str_names[n])
  paths.append(f"/input/FASTA_Files/{str_names[n]}.fa")
  num_add_strains = int(vec_names[n][1])
  total_num_genomes = num_add_strains+1

  for o in range(0, int(num_add_strains)):
    strain_name = f"{str_names[n]}_S{o}"
    genomes.append(strain_name)
    paths.append(f"/input/FASTA_Files/{strain_name}.fa")

  OTU_list = list(range(0, total_num_genomes))
  NCBIID_list = [717605]*total_num_genomes
  novelty_list = ["new_species"]*total_num_genomes

  metadata_file = f"metadata_{n}.tsv"
  rows = list(zip(genomes, OTU_list, NCBIID_list, novelty_list))
  with open(metadata_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    header = ["genome_ID", "OTU", "NCBI_ID", "novelty_category"]
    writer.writerow(header)
    writer.writerows(rows)

  id_to_genome_file = f"id_to_genome_{n}.tsv"
  rows = list(zip(genomes, paths))
  with open(id_to_genome_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(rows)

  lens.append(len(genomes))

print(lens)