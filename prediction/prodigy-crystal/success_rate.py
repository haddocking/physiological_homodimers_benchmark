#!/usr/bin/env python3

import os
import sys


def parse_prediction(file_name):
    with open(file_name) as input_handle:
        for line in input_handle:
            if line.startswith('[+] Class'):
                return line.split()[2]
        return None


if __name__ == "__main__":
    complex_list_file = sys.argv[1]
    physiological_list_file = sys.argv[2]
    nonphysiological_list_file = sys.argv[3]

    complex_list = []
    physiological_list = []
    nonphysiological_list = []

    with open(complex_list_file) as input_handle:
        complex_list = [line.rstrip(os.linesep) for line in input_handle.readlines() if line]

    with open(physiological_list_file) as input_handle:
        physiological_list = [line.rstrip(os.linesep) for line in input_handle.readlines() if line]

    with open(nonphysiological_list_file) as input_handle:
        nonphysiological_list = [line.rstrip(os.linesep) for line in input_handle.readlines() if line]

    print(f'Size of complex list: {len(complex_list)}')
    print(f'Size of Physiological list: {len(physiological_list)}')
    print(f'Size of Non Physiological list: {len(nonphysiological_list)}')

    bio_predicted = []
    crystal_predicted = []

    for pdb_id in complex_list:
        prediction_out = f'{pdb_id}.out'
        prediction = parse_prediction(prediction_out)
        if not prediction:
            raise SystemExit(f'Prediction not found for {prediction_out}')
        elif prediction == 'BIO':
            bio_predicted.append(pdb_id)
        else:
            crystal_predicted.append(pdb_id)

    print(f'Predicted as BIO and Physiological: {len(set(bio_predicted) & set(physiological_list))}')
    print(f'Predicted as BIO and Non-Physiological: {len(set(bio_predicted) & set(nonphysiological_list))}')
    print(f'Predicted as CRYSTAL and Physiological: {len(set(crystal_predicted) & set(physiological_list))}')
    print(f'Predicted as CRYSTAL and Non-Physiological: {len(set(crystal_predicted) & set(nonphysiological_list))}')
    print()
    success_rate = (len(set(bio_predicted) & set(physiological_list)) + len(set(crystal_predicted) & set(nonphysiological_list))) / len(complex_list) * 100.
    print(f'Success rate: {round(success_rate, 2)}%')
