# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:08:56 2019

@author: Adnan
"""

import os
import random
import hdf5storage
import numpy as np

DATASET_PATH = "D:/Dataset/Multi-resolution_data/Visual/High/"

train_images = []
test_images = []
train_i = []
test_i = []
train_label = list()
test_label = list()
percent_train = 0.4
class_folders = next(os.walk(DATASET_PATH))[1]
for x in class_folders:
    files = os.listdir(os.path.join(DATASET_PATH, x))
    random.shuffle(files)
    n = int(len(files) * percent_train)

    for i, f in enumerate(files):
        abs_path = os.path.join(DATASET_PATH, x, f)
        mat = hdf5storage.loadmat(abs_path)
        if (i < n):
            train_i.append(mat.values())
            train_label.append(x)
        else:
            test_i.append(mat.values())
            test_label.append(x)

    train_images.append(train_i)
    test_images.append(test_i)

    # tt= np.stack(train_i, axis=2)
