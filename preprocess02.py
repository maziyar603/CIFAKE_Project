import numpy as np
import glob
import os
from icecream import ic
import json

lable_map = {'fake_train':0 ,'real_train':1,'fake_test':0,'real_test':1}
root_folder = '../CF_IMAGE'
train_FakeFolder = 'fake_train'
train_RealFolder = 'real_train'
test_RealFolder = 'real_test'
test_FakeFolder = 'fake_test'

def create_json(folder,json_filename,labels):
    files = glob.glob(os.path.join(root_folder,folder,'*'))
    data = {'images': files, 'labels': [labels]*len(files)}
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=4)

create_json(folder = 'fake_train',json_filename ='fake_train_data.json',labels=0 )
create_json(folder = 'real_train',json_filename ='real_train_data.json',labels=1 )
create_json(folder = 'real_test',json_filename ='real_test_data.json',labels=1 )
create_json(folder = 'fake_test',json_filename ='fake_test_data.json',labels=0 )







    