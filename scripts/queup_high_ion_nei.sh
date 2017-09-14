#!/bin/bash

#PBS -j oe
#PBS -N noaa1109_tn750ion_calc_nei

echo "Starting run at `date`"

export XUVTOP="/usr/local/ssw/packages/chianti/dbase"

PYTHON=/home/wtb2/anaconda3/envs/systematic-ar-study/bin/python
SCRIPT_DIR=/home/wtb2/Documents/projects/systematic_ar_study/scripts/
ROOT='/data/datadrive2/ar_viz/systematic_ar_study/'
FREQ_DIR="noaa1109_tn750-ion/"
FIELD_PATH=$ROOT$FREQ_DIR"field_checkpoint"
EM_MODEL_PATH="/data/datadrive1/ar_forward_modeling/systematic_ar_study/emission_model1109_full"
NEI_SAVE=$ROOT$FREQ_DIR"loop_nei.h5"

$PYTHON $SCRIPT_DIR"calculate_fractional_ionization.py" -f $FIELD_PATH -e $EM_MODEL_PATH -n $NEI_SAVE

echo "Finished run at `date`"
