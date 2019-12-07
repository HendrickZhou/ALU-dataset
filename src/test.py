
from ALU import *
import pickle
import numpy as np

batch_name = lambda idx : "ALU-8-14_batch_" + str(idx) + ".batch"
folder_path = "/Users/zhouhang/Project/ALU-dataset/dataset/"

def read_patch(path, filename):
    with open(path + filename, 'rb') as f:
        batch=pickle.load(f)

    data = batch['data']
    label = batch['label']
    return data, label

def read_patch_folder(path):
    data, label = read_patch(path, batch_name(1))
    print(data.dtype)
    print(label.shape)


read_patch_folder(folder_path)
