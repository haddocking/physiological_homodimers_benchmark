#!/usr/bin/env python3

import os
import sys


def parse_file_prediction(file_name):
    """Parses a PRODIGY-CRYSTAL result file (*.out)"""
    with open(file_name) as input_handle:
        for line in input_handle:
            if line.startswith('[+] Class'):
                pclass, p1, p2 = line.split()[2:]
                if pclass == 'XTAL':
                    pclass = 'crystal'
                else:
                    pclass = 'biological'
                return (pclass, p1, p2)
        return None


if __name__ == "__main__":
    """Writes in CSV format"""
    complex_list_file = sys.argv[1]

    complex_list = []
    with open(complex_list_file) as input_handle:
        complex_list = [line.rstrip(os.linesep) for line in input_handle.readlines() if line]

    print('#pdb_id,prodigy_crystal_class,p_biological,p_crystal')
    for pdb_id in complex_list:
        prediction_out = f'{pdb_id}.out'
        prediction = parse_file_prediction(prediction_out)
        if not prediction:
            raise SystemExit(f'Prediction not found for {prediction_out}')
        else:
            print(f'{pdb_id},{prediction[0]},{prediction[1]},{prediction[2]}')
