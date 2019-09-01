
'''
Split the image chips in 70%train, 20%test and 10% validation data folders.

The script loops over all the chips and masks in the folders for each date
It loads each image and its mask, checks if the mask is empty or has features
If the mask is empty, it continues to next iteration of the loop
Else, it copies into respective train, test or validation folder

'''
import os
from PIL import Image
import glob
import json
from numpy import asarray, expand_dims, savez_compressed
import numpy as np
from skimage import io
import random
import h5py
import shutil

# Dictionary to loop over the dates of imagery
paths = {
        '20180515':'D:\\home\\uceshaf\\FinalProject\\datasets\\Mosaic2_20180515\\',
        '20180420':'D:\\home\\uceshaf\\FinalProject\\datasets\\Mosaic1_20180420\\'
        '20180727':'D:\\home\\uceshaf\\FinalProject\\datasets\\Mosaic3_20180727\\',
        '20181011':'D:\\home\\uceshaf\\FinalProject\\datasets\\Mosaic4_20181011\\',
        }

print(paths)

# the following function to load all images into memory
def load_dataset(path, imgfolder, lblfolder, imglist):
        emptydict={}
        print('In load data')
        images, labels = list(), list()
        # enumerate files in the directory
        for imgname in imglist:
                #print(str(imgname))
                img = io.imread(path+imgfolder+imgname)
                # Check if image is of background values only
                if 0 in np.min(img, axis=tuple(range(img.ndim-1))):
                        print('No Data Values Found')
                        continue
                #convert to numpy array
                img = img_to_array(img)#, dtype='uint8')
                #Now read for label masks
                lbl = io.imread(path+lblfolder+imgname)
                # Check if the mask is empty
                if lbl.max() == 0:
                        emptydict.update({path+imgfolder+imgname:path+lblfolder+imgname})
                        #If mask is empty, move to next iteration
                        continue
                lbl = expand_dims(lbl, axis = 2)
                images.append(img)
                labels.append(lbl)
        print('saving the 16-bit values')
        X = asarray(images)#, dtype = 'uint8')
        y = asarray(labels)#, dtype= 'uint8')
        return X, y, emptydict

random.seed(9289)

# Loop to split the list of images into train, test and validation folders
for date,path in paths.items():
        imgfolder = 'images\\'
        lblfolder = 'labels\\'
        print(path)
        # dictionary of folders
        folders = {
        'traini': 'train/tifs/images/',
        'trainm' : 'train/labels/masks/',
        'testi' : 'test/tifs/images/',
        'testm' : 'test/labels/masks/',
        'vali' : 'val/tifs/images/',
        'valm' : 'val/labels/masks/'
        }
        # create folders of they don't exist
        for folder, fpath in folders.items():
                if not os.path.exists(path+fpath):
                        os.makedirs(path+fpath)
                
        os.chdir(path+imgfolder)
        # get the image list
        imglist = glob.glob('*.tif')
        imglist.sort()
        # Shuffling so that random images are given to model rather than the sequence
        random.shuffle(imglist)
        print(imglist[1:10])
        N = len(imglist)
        print('\n\nTotal number of images for date : ',str(date),' are ',str(N))
        # create indices for train, test and validation data
        t = int(N/5000)+1
        trg = int(N*0.7)+1
        test = int(N*0.9)+1
        val = N
        print(trg,test,val)
        alllists = {
        'traini': imglist[0:trg],
        #'trainm' : imglist[0:trg],
        'testi' : imglist[trg: test],
        #'testm' : imglist[trg: test],
        'vali' : imglist[test: N],
        #'valm' : imglist[test: N]
        }

emptydict={}
for name, ilist in alllists.items():
        print(name)
        for imgname in ilist:
                img = io.imread(path+imgfolder+imgname)
                # Check if image is of background values only
                if 0 in np.min(img, axis=tuple(range(img.ndim-1))):
                        print('No Data Values Found',imgname)
                        #If img is empty, move to next iteration
                        continue
                lbl = io.imread(path+lblfolder+imgname)
                # Check if the mask is empty
                if lbl.max() == 0:
                        emptydict.update({path+imgfolder+imgname:path+lblfolder+imgname})
                        print('empty classes',imgname)
                        #If mask is empty, move to next iteration
                        continue
                # copy the image with its mask to the respective folders
                shutil.copy2(path+imgfolder+imgname, path+folders[name]+imgname)
                shutil.copy2(path+lblfolder+imgname, path+folders[name[:-1]+'m']+imgname)


print(emptydict)
