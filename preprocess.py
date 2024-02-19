import os
from icecream import ic
import json
root_folder = '../CF_IMAGE'
train_FakeFolder = 'fake_train'
train_RealFolder = 'real_train'
test_RealFolder = 'real_test'
test_FakeFolder = 'fake_test'

labels_map = {'fake_train': 0, 'real_train': 1, 'real_test': 1, 'fake_test': 0}
train_data = {'images': [], 'labels': []}
test_data = {'images': [], 'labels': []}

for folder in ['fake_train', 'real_train', 'real_test', 'fake_test']:
    data_folder_str = os.path.join(root_folder, folder)
    files = os.listdir(data_folder_str)
    new_files = []
    labels = []
    for my_files in files:
        new_files.append(os.path.join(root_folder, folder, my_files))
        labels.append(labels_map[folder])
    
    if folder == 'fake_train'or folder == 'real_train':
        train_data['images'].extend(new_files)
        train_data['labels'].extend(labels)
    else:
        test_data['images'].extend(new_files)
        test_data['labels'].extend(labels)

# ic(train_data)
# ic(test_data)
with open('train_data01.json','w') as f:
    json.dump(train_data,f , indent=4)
    
with open('test_data01.json','w') as f:
    json.dump(test_data,f,indent=4)    
    







