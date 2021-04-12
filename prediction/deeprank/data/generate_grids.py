"""
Generate deepface HDF5 dataset.

Author: {0} ({1})
"""
import os
import sys
import numpy as np 
from deeprank.generate import *
#  from mpi4py import MPI

__author__ = "Cunliang Geng"
__email__ = "gengcunliang AT gmail.com"
USAGE = __doc__.format(__author__, __email__)


def check_input(args):
    if len(args) != 3:
        sys.exit(USAGE)


def generate_dataset(pdb_source, pssm_source, h5out):

    #  comm = MPI.COMM_WORLD

    if os.path.isfile(h5out):
        os.remove(h5out)

    database = DataGenerator(pdb_source=pdb_source,
                            pssm_source=pssm_source,
                            compute_features = ['deeprank.features.AtomicFeature',
                                                'deeprank.features.FullPSSM',
                                                'deeprank.features.PSSM_IC',
                                                'deeprank.features.BSA',
                                                'deeprank.features.ResidueDensity'],
                            data_augmentation = 1, # rotate complexes
                            hdf5=h5out)

    #create new files
    database.create_database()

    # map the features
    grid_info = {
       'number_of_points': [10, 10, 10],
       'resolution': [3., 3., 3.],
       'atomic_densities': {'C': 1.7, 'N': 1.55, 'O': 1.52, 'S': 1.8},
    }
    database.map_features(grid_info, try_sparse=True, time=False, prog_bar=True)

    # add target
    database.add_unique_target({'BIN_CLASS':1})

if __name__ == '__main__':

    np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
    check_input(sys.argv[1:])
    pdb_source, pssm_source, h5out = sys.argv[1:]
    generate_dataset(pdb_source, pssm_source, h5out)
