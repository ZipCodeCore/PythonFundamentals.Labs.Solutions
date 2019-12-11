import json
import os
import pandas as pd


def read_json(file_path):
    json_input = None
    with open(file_path) as f:
        json_input = json.load(f)
    return json_input


def read_all_json_files(json_root):
    for root, _, files in os.walk(json_root):
        result = pd.DataFrame()
        for f in files:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(json_root, f))
                temp_df = pd.DataFrame(json_content['results'])
                temp_df['source'] = f
                result = result.append(temp_df)
    return result
