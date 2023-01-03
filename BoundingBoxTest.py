#!/usr/bin/env python
# coding: utf-8

# # Setup

# In[23]:


from PIL import Image, ImageFile, ImageDraw, ImageFont
import json
import time 
import timeit
import numpy as np

# what colors to use to display bounding boxes
# clases that are not in this dictionary will not be displayed
color_dict = {
    "Lung Opacity": '#ff6769',
    "Atelectasis": '#a87e56',
    "Consolidation": '#6bdd7b',
    "Fracture": '#82bde9',
    "Lung Lesion": '#eb69a5',
    "Pleural Effusion": '#8353a5',
    "Pleural Other": '#ffaa4d',
    "Tuberculosis": '#f4f156',
    "Pneumothorax": '#0392ce'
}

# the labels to be displayed next to each of the classes' bounding boxes
label_dict = {
    "BBOX_Atelectasis": "AT",
    "BBOX_Consolidation": "CO",
    "BBOX_Fracture": "FR",
    "BBOX_Lung Lesion": "LL",
    "BBOX_Lung Opacity": "LO",
    "BBOX_Pleural Effusion": "PE",
    "BBOX_Pleural Other": "PO",
    "BBOX_Pneumothorax": "PX",
    "BBOX_Tuberculosis": "TBC",
}

bboxes_width = 2 # width of bounding box sides
text_scale = 60 # size of the bounding box labels
benchmark_runs = 50 # how many times to run the drawing benchmark


# # Benchmark

# In[25]:


test_img_path = 'img.jpeg'
test_bbox_path = 'bounding_boxes.json'

img = Image.open(test_img_path).convert('RGB')
print(f'Loaded image {test_img_path}, shape: {img.size}')

# we scale the text according to the image dimensions and the scale
# the fnt object is used to draw text
text_size = img.height // text_scale * img.width // img.height
fnt = ImageFont.truetype("arial.ttf", int(text_size))

with open(test_bbox_path, 'r') as file:
    bbox_list = json.load(file)
print(f'Loaded {sum([len(l) for l in bbox_list])} BBoxes from {test_bbox_path}')
print(f'First BBox class {bbox_list[0]}')

benchmark_times = []
for benchmark_idx in range(benchmark_runs):
    # this is used to draw on the image
    # draw.rectangle and draw.text draw rectangles and text directly on the pixels of an image
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)

    a = timeit.default_timer()

    # go through each bbox_dict, each entry contains the class name and a list of rectangles representing the bounding boxes
    for bbox_dict in bbox_list:
        bbox_class = bbox_dict['type']

        # skip bounding boxes that are not meant to be displayed or that have no rectangles
        if bbox_class not in color_dict or len(bbox_dict['rectangles']) == 0:
            continue

        label_size = fnt.getsize(label_dict['BBOX_' + bbox_class])
        # label_size = (width, height) of the label text

        # go through each rectangle of the class
        for bbox in bbox_dict['rectangles']:
            draw.rectangle((bbox['start']['x'], bbox['start']['y'], bbox['end']['x'], bbox['end']['y']), outline=color_dict[bbox_class], width=bboxes_width)

            # MODIFY THIS
            # these are the coordinates at which we draw the label
            label_spot = bbox['start']['x'], bbox['start']['y'] - label_size[1] * 1.2
            draw.text(label_spot, label_dict['BBOX_' + bbox_class], font=fnt, fill=color_dict[bbox_class])

    b = timeit.default_timer()
    benchmark_time = b - a
    benchmark_times.append(benchmark_time)
    print(f'Benchmark {benchmark_idx} run time {b - a:.5f}s')
        
b_mean, b_std = np.mean(benchmark_times), np.std(benchmark_times)
print(f'Benchmark done, {benchmark_runs} runs, mean time {b_mean:.5f} (+/- {b_std:.5f})s')
        
img_copy.save('./out.jpg')
print('Saved image to out.jpg')


# In[ ]:




