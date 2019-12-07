#!/usr/bin/env python

from ALU import *
import numpy as np
import pickle

class Dataset():
    def __init__(self, filename, path):
    	self.path = path
    	self.filename = filename

    def __call__(self):
    	# op_list = ['', '', '']
    	big_brain = ALU(8) # gonna use the default params
    	number, ops = big_brain.gen_range()
    	datas = []
    	labels = []
    	batch_size = 5000
    	data_dim = big_brain.data_dim
    	label_dim = big_brain.label_dim
    	total_size = len(ops) * len(number)**2
    	print(total_size)
    	i = 0
    	for op in ops:
    		for B in number:
    			for A in number:
    				in1, in2, opc, out = big_brain(A, B, op)
    				# arr = lambda a : np.array(list(a), dtype="uint8")
    				data = list(in1) + list(in2) + list(opc)
    				# print(data.shape)
    				datas.append(data)
    				label = list(out)
    				# print(label.shape)
    				# if len(out) is 7:
    				# 	print(op)
    				# 	print(in1)
    				# 	print(in2)
    				# 	print(out)
    				labels.append(label)
    				i = i + 1
    				if i%batch_size is 0 or i is total_size:
				    	name = self.filename + "_"+ str(i//batch_size)
				    	actual_size = batch_size if i % batch_size is 0 else i % batch_size
    					data_arr = np.array(datas, dtype= 'uint8').reshape((actual_size, data_dim))
				    	label_arr = np.array(labels, dtype = 'uint8').reshape((actual_size, label_dim))
				    	dataset = dict()
				    	dataset["data"] = data_arr
				    	dataset["label"] = label_arr
				    	with open(self.path + name + '.batch', 'wb+') as f:
				    		pickle.dump(dataset, f, protocol=pickle.HIGHEST_PROTOCOL)
				    	datas = []
				    	labels = []
         



if __name__ == '__main__':
	import os
	script_path = os.path.abspath(__file__)
	project_dir = script_path[:script_path.rfind("src")]
	output_path = project_dir + "dataset/"
	ds = Dataset("ALU-8-14_batch", output_path)
	ds()
