import numpy as np
import os
import json
import glob
from icecream import ic
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_folder', default='../CF_IMAGE', type=str, required=False, help='Root folder of the data')


parser.add_argument('--fake_train_save_filename', default='fake_train.json', type=str, required=False, help='Filename to save the train data')
parser.add_argument('--real_train_save_filename', default='real_train.json', type=str, required=False, help='Filename to save the train data')
parser.add_argument('--real_test_save_filename', default='real_test.json', type=str, required=False, help='Filename to save the train data')
parser.add_argument('--fake_test_save_filename', default='fake_test.json', type=str, required=False, help='Filename to save the test data')
args = parser.parse_args()
class PrepareData:
    def __init__(self,):
        self.root_folder = args.root_folder
    def create_json(self, folder):
        data = {}
        file_paths = glob.glob(os.path.join(self.root_folder, folder,'*'))
            
        #labels = [0 if my_file.split('\\')[-2] =='fake'  else 1 for my_file in file_paths ]
        labels = [0 if 'fake' in my_file.split('\\')[-2] else 1 for my_file in file_paths]
        data['images'] = file_paths
        data['labels'] = labels
        if folder == 'fake_train':
            save_filename = args.fake_train_save_filename
        elif folder == 'real_train':
            save_filename = args.real_train_save_filename
        elif folder == 'real_test':
            save_filename = args.real_test_save_filename
        elif folder == 'fake_test':
            save_filename = args.fake_test_save_filename   
        with open(save_filename, 'w') as f:
                json.dump(data, f, indent=4)

data_preparer = PrepareData()
data_preparer.create_json(folder='fake_train')
data_preparer.create_json(folder='real_train')
data_preparer.create_json(folder='real_test')
data_preparer.create_json(folder='fake_test')














