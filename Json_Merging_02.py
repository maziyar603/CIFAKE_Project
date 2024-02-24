import json
from icecream import ic

def merge_json_files(input_files, output_file):
    # Define the structure of the JSON file
    merged_data = {'images': [], 'labels': []}

    for input_file in input_files:
        
        with open(input_file, 'r') as f:
            data = json.load(f)
            merged_data['images'].extend(data.get('images', []))
            merged_data['labels'].extend(data.get('labels', []))
    
            with open(output_file, 'w') as f:
                json.dump(merged_data, f, indent=4)
                ic(f"Merged JSON file saved as '{output_file}'.")

# Define input and output file paths
input_files_test = ['fake_test.json', 'real_test.json']
output_file_test = 'TEST_data.json'

input_files_train = ['fake_train.json', 'real_train.json']
output_file_train = 'TRAIN_data.json'

# Merge test data
merge_json_files(input_files_test, output_file_test)

# Merge train data
merge_json_files(input_files_train, output_file_train)


