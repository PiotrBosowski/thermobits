import os
import json


"""
Darknet wants a .txt file for each image with a line for each ground
truth object in the image that looks like:
<object-class> <x> <y> <width> <height>
Where x, y, width, and height are relative to the image's width and h.
"""

for subset in ['train', 'val', 'video']:
    images_path = os.path.join('FLIR_ADAS_1_3', subset,
                               'Annotated_thermal_8_bit')
    annotations_path = os.path.join('FLIR_ADAS_1_3', subset,
                                    'thermal_annotations.json')
    with open(annotations_path, 'r') as json_file:
        border_dict = json.load(json_file)
    for image in border_dict['images']:
        current_annotations = [annot for annot in border_dict['annotations']
                               if annot['image_id'] == image['id']]
        image_name = os.path.basename(image['file_name'])
        base, ext = os.path.splitext(image_name)
        with open(os.path.join(images_path, base + ".txt"), 'x') as file:
            for annot in current_annotations:
                category = annot['category_id']
                x = (annot['bbox'][0] + annot['bbox'][2] / 2) / image['width']
                y = (annot['bbox'][1] + annot['bbox'][3] / 2) / image['height']
                width = annot['bbox'][2] / image['width']
                height = annot['bbox'][3] / image['height']
                darknet_format = f"{category} {x} {y} {width} {height}\n"
                file.write(darknet_format)

