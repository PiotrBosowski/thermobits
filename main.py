import os
import json

# Darknet wants a .txt file for each image with a line for each ground
# truth object in the image that looks like:
# <object-class> <x> <y> <width> <height>
# Where x, y, width, and height are relative to the image's width and height.
from collections import namedtuple
from dataclasses import dataclass


with open('./thermal_annotations.json') as json_file:
    border_dict = json.load(json_file)
os.makedirs('darknet-annotations', exist_ok=True)
for image in border_dict:
    annotations = [annot for annot in border_dict['annotations']
                   if annot['image_id'] == image['id']]
    file_name = os.path.basename(image['file_name'])
    name, ext = os.path.splitext(file_name)
    with open(name + ".txt", 'x') as file:
        for annot in annotations:
            category = annot['category_id']
            x = (annot['bbox'][0] + annot['bbox'][2] / 2) / image['width']
            y = (annot['bbox'][1] + annot['bbox'][3] / 2) / image['height']
            width = annot['bbox'][2] / image['width']
            height = annot['bbox'][3] / image['height']
            darknet_format = f"{category} {x} {y} {width} {height}\n"
            file.write(darknet_format)



