#!/bin/bash

#PBS -j oe
#PBS -N noaa1109_tn250_flatten_counts

echo "Starting run at `date`"

export XUVTOP="/usr/local/ssw/packages/chianti/dbase"

PYTHON=/home/wtb2/anaconda3/envs/systematic-ar-study/bin/python
SCRIPT_DIR=/home/wtb2/Documents/projects/systematic_ar_study/scripts/
ROOT='/data/datadrive1/ar_forward_modeling/systematic_ar_study/'
FREQ_DIR="noaa1109_tn250/"
FIELD_PATH=$ROOT$FREQ_DIR"field_checkpoint"
EM_MODEL_PATH=$ROOT"emission_model1109_full"

$PYTHON $SCRIPT_DIR"flatten_detector_counts.py" -f $FIELD_PATH -e $EM_MODEL_PATH -d $ROOT$FREQ_DIR

echo "Finished run at `date`"
