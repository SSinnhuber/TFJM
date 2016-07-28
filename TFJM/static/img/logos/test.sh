#!/bin/bash

for img in `ls *.jpg *.png *.gif`
do
	convert $img -resize 200x150 thumbnail/$img
done
