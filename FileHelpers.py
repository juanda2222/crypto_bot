import json
import os

from Constants import DEFAULT_SAVE_TO_FILES

# helper file functions
def write_to_json_file(filename, data, save_on_files = DEFAULT_SAVE_TO_FILES):
    path = 'files/{}.json'.format(filename)
    if not os.path.exists('files'):
        os.makedirs('files')

    if save_on_files:
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=2)
