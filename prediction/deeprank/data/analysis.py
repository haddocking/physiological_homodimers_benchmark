import glob
import os 
import sys
import h5py 
import numpy as np 
import torch 

output = open('deeprank_predictions.txt', 'w')
output.write('pdb class p_crystal p_bio \n')

for hdf5 in glob.glob('*/'):
    name=hdf5.split('/')[0]
        
    if os.path.exists('{}test_data.hdf5'.format(hdf5)):
        
        f = h5py.File('{}test_data.hdf5'.format(hdf5),'r')
        
        results = f['epoch_0000']['test']['outputs'][()]
        res = results[0]
        softmax = torch.nn.Softmax(dim=0)
        res_softmax = softmax(torch.Tensor(res)).numpy()
        
        bin_class_res = np.argmax(res)
        
        if bin_class_res1 == 0 : 
            pred = 'crystal'
            
        else :
            pred = 'biological'

        output.write(name+" "+pred+" "+str(bin_class_res)+" "+str(round(res_softmax[0],3))+" "+str(round(res_softmax[1],3))+"\n")

    else:
        output.write(name+" None None None None \n")

output.close()
