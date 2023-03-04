#!/bin/bash
conda activate snippet 
source ~/.bashrc

notedir=`pwd`
export PATH=/root/go/bin:$PATH 
jupyter-lab --allow-root --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.ip='0.0.0.0' --NotebookApp.notebook_dir="${notedir}"
