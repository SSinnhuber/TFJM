#!/bin/bash

for image in `ls *.JPG`
do
	convert $image -resize 67% ../$image
done
