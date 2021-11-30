import json
import os
import pandas

def directory_browser(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    return files, folders


def read_json(file_name, debug=False):
    with open(file_name, 'r') as f:
        data = json.load(f)
        if debug:
            return data, os.stat(file_name)
    return data

def write_json(file_name, data, debug=False):
    with open(file_name, 'w') as f:
        json.dump(data, f)
        if debug:
            return os.stat(file_name)

def read_excel(file_name, debug=False):
    df = pandas.read_excel(file_name, 0, 48)
    if debug:
        return df, os.stat(file_name)
    return df