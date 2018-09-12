## Introduction

A Keras implementation of YOLOv3 (Tensorflow backend) on [bdd100k dataset](http://bair.berkeley.edu/blog/2018/05/30/bdd/).

---

## Guide

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to Keras model.
3. Run YOLO detection.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5
python yolo.py   OR   python yolo_video.py [video_path] [output_path(optional)]
```
---

## Choice of Anchor Boxes

YOLO v3, in total uses 9 anchor boxes. Three for each scale. If training YOLO on a custom dataset, generation of anchors must be done using K-Means clustering.
Then, arrange the anchors is descending order of dimensions. Assign the three biggest anchors for the first scale , the next three for the second scale, and the last three for the third.

---

## Training

1. Generate the annotation file using `python bdd100k_annotation.py` and class names file.  
    One row for one image;  
    Row format: `image_file_path box1 box2 ... boxN`;  
    Box format: `x_min,y_min,x_max,y_max,class_id` (no space).  
    For example:
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```

2. Make sure you have run `python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5`  
    The file model_data/yolo_weights.h5 is used to load pretrained weights.

3. Modify train.py and start training.  
    `python train.py`  
    Use your trained weights or checkpoint weights in yolo.py.  
    Remember to modify class path or anchor path.
    
---
