"""
Test 3DeepFace models

"""
import os
import sys
import glob
from deeprank.learn import *

# to set your own architecture
from arch_001_02 import cnn_class as cnn3d_class

################################################################################
# input and output settings
################################################################################

# You need to add path for the dataset
database = glob.glob('./*hdf5')
output = open('errors.txt', 'w')

for complx in database :
    # You need to set it as your output path
    name=complx.split('/')[-1].split('.')[0]

    if os.path.exists('output/{}'.format(name)) :
        continue
    
    else:
        os.mkdir('output/')
        os.mkdir('output/{}'.format(name))
        
        outpath = 'output/{}'.format(name)
        
        ################################################################################
        # Start the training
        ################################################################################
        try:
            model = NeuralNet(complx,cnn3d_class,pretrained_model='best_model.pth.tar', outdir=outpath)
            model.test()

        except:
            output.write('prediction on {} failed'.format(name))

output.close()
