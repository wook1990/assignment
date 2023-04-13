#!/bin/bash
python cut_image.py $1 $2 $3
python merge_image.py $1 $2
