import os
import logging
import argparse

import astropy.units as u
import numpy as np

import synthesizAR
from synthesizAR.atomic import EmissionModel
from synthesizAR.instruments import InstrumentSDOAIA,InstrumentHinodeEIS

parser = argparse.ArgumentParser()
parser.add_argument("-e","--em_model_path",help="path to emission model")
parser.add_argument("-f","--field_path",help="path to field")
parser.add_argument("-d","--detector_counts_path",help="top level directory to save flattened counts in")
args = parser.parse_args()

# restore field
field = synthesizAR.Skeleton.restore(args.field_path)
# restore emission model
emission_model = EmissionModel.restore(args.em_model_path)

# create instruments
observing_time = [0,2e4]*u.s
aia = InstrumentSDOAIA(observing_time,
                       use_temperature_response_functions=False,
                       emission_model=emission_model
                      )
eis = InstrumentHinodeEIS(observing_time)

# create observer
ds = field._convert_angle_to_length(0.4*u.arcsec)
observer = synthesizAR.Observer(field,[eis,aia],ds=ds)

observer.logger.setLevel(logging.DEBUG)

# build detector files
observer.build_detector_files(args.detector_counts_path)

# flatten detector counts
observer.flatten_detector_counts()