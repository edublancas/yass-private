#!/usr/bin/env bash
MACHINE=spike-sorter 

gcloud compute scp $MACHINE:~/data/detect/models/ \
    ~/Desktop/models --zone us-east1-c --recurse