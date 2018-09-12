import argparse
import json
import os
from os import path as osp
from os import getcwd
import sys

classes = ["person"]

def parse_args():
    """Use argparse to get command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('label_dir', help='path to the label dir')
    args = parser.parse_args()

    return args


def label2det(label):
    f = open('val.txt', 'a+')
    f.write('/media/erress/Personal/Programming/BennettUniversity/bdd100k/images/100k/val/%s.jpg' % (label['name']))
#    f.write('%s/bdd100k/images/100k/train/%s.jpg' % (wd,label['name']))
    for frame in label['frames']:
        for obj in frame['objects']:
            if 'box2d' not in obj:
                continue
            xy = obj['box2d']
            cls = obj['category'] 
            if cls not in classes:
                continue
            cls_index = classes.index(cls)
            if xy['x1'] >= xy['x2'] and xy['y1'] >= xy['y2']:
                continue
            box_info = " %d,%d,%d,%d,%d" % (xy['x1'], xy['y1'], xy['x2'], xy['y2'],cls_index)            
            f.write(box_info)
    f.write('\n')
    f.close()


def change_dir(label_dir):
    if not osp.exists(label_dir):
        print('Can not find', label_dir)
        return
    print('Processing', label_dir)
    input_names = [n for n in os.listdir(label_dir)
                   if osp.splitext(n)[1] == '.json']
    wd = getcwd()
    count = 0
    for name in input_names:
        in_path = osp.join(label_dir, name)
        label2det(json.load(open(in_path, 'r')))
#        label2det(json.load(open(in_path, 'r')),wd)
        count += 1
        if count % 1000 == 0:
            print('Finished', count)
    

def main():
    args = parse_args()
    change_dir(args.label_dir)


if __name__ == '__main__':
    main()
