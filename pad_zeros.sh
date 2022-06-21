#!/bin/bash
IFS=:
for i in *.mp4 ; do
    mv $i `printf '%04d' ${i%.jpg}`.jpg
done
