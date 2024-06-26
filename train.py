from PIL import Image
import numpy as np
import time
from utils import printProgressBar
def normalizeMasks(files):
    print("Normalize masks")
    tic = time.time() 
    for k,file in enumerate(files):
        printProgressBar(k,len(files))
        img = Image.open(file)
        arr = np.array(img)
        indexes = np.sort(np.unique(arr))
        normalized = range(0,len(indexes)+1)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                pixel = arr[i,j]
                if(pixel == 0):
                    continue
                ind = np.where(indexes == pixel)[0]
                if(len(ind) > 1):
                    print("Warning: One mask has the same index of another")
                ind = ind[0]
                arr[i,j] = normalized[ind]
        norm_img = Image.fromarray(arr)
        #timee = file.split("t00")[1].split("xy")[0]
        timee = file.split("_")[1]
        #ds = file.split("t00")[0]
        ds = file.split("_")[0]
        norm_img.save(ds+"_"+timee+"_mask_.tif")
    net_time = time.time() - tic
    print(f'Normalization done ({np.round(net_time,2)}s)')

from omnipose.utils import normalize99
def normalizeImgs(files):
    print("Normalize raws")
    tic = time.time() 
    for k,file in enumerate(files):
        printProgressBar(k,len(files))
        img = Image.open(file)
        arr = np.array(img)
        arr = normalize99(arr)
        norm_img = Image.fromarray(arr)
        wthout_tif = file.split(".")[0]
        #timee = file.split("t00")[1].split("xy")[0]
        timee = wthout_tif.split("_")[1]
        #ds = file.split("t00")[0]
        ds = wthout_tif.split("_")[0]
        norm_img.save(ds+"_"+timee+"_.tif")
    net_time = time.time() - tic
    print(f'Normalization done ({np.round(net_time,2)}s)')

"""
<<<<<<< Updated upstream
omnipose --train --use_gpu --dir ~/Documents/Training/ --mask_filter _mask --n_epochs 4000 --learning_rate 0.1 --diameter 0 --batch_size 8  --RAdam --nclasses 3
=======
omnipose --train --use_gpu --dir C:\Users\abc\Documents\Stage24\Training --mask_filter _mask --n_epochs 5000 --pretrained_model bact_phase_omni --learning_rate 0.1 --diameter 0 --batch_size 18  --RAdam --nclasses 3
>>>>>>> Stashed changes
"""
