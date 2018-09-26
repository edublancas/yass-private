#!/usr/bin/env bash
MACHINE=spike-sorter 

gcloud compute scp $MACHINE:~/data/denoiser/figs \
    ~/Desktop/figs --zone us-east1-c --recurse