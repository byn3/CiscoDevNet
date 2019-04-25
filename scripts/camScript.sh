#!/bin/bash
echo "START"
filename=$( python cam.py)
mv $filename photos/
echo "$filename" >> photos/photos.txt
echo $(curl -v -F image=@photos/$filename http://localhost:8084/classifyImage)
#echo "$filename" >> mlphotos/mlphotos.txt
