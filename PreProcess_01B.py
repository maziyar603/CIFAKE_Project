import os
import json
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_folder', default='../CF_IMAGE', type=str, required=False, help='Root folder of the data')
parser.add_argument('--save_folder', default='../', type=str, required=False, help='Folder to save the JSON files')
args = parser.parse_args()

class PrepareData:
    def __init__(self, root_folder, save_folder):
        self.root_folder = root_folder
        self.save_folder = save_folder

    def create_json(self, folder):
        data = {}
        file_paths = glob.glob(os.path.join(self.root_folder, folder, '*'))
        labels = [0 if 'fake' in file_path.split(os.path.sep)[-2] else 1 for file_path in file_paths]
        data['images'] = file_paths
        data['labels'] = labels
        save_filename = os.path.join(self.save_folder, f'{folder}.json')
        with open(save_filename, 'w') as f:
            json.dump(data, f, indent=4)

data_preparer = PrepareData(args.root_folder, args.save_folder)
data_preparer.create_json('fake_train')
data_preparer.create_json('real_train')
data_preparer.create_json('real_test')
data_preparer.create_json('fake_test')
