import os
import argparse

import synthesizAR
from synthesizAR.model_ext import EbtelInterface
from synthesizAR.atomic import EmissionModel


parser = argparse.ArgumentParser()
parser.add_argument("-e","--em_model_path",help="path to emission model")
parser.add_argument("-f","--field_path",help="path to field")
parser.add_argument("-n","--nei_save",help="file to save nei results in")
args = parser.parse_args()

# restore field and emission model
field = synthesizAR.restore(args.field_path)
emiss_model = EmissionModel.restore(args.em_model_path)

#create dummy ebtel interface for calculating NEI populations
class DummyHeatingModel(object):
    def __init__(self):
        self.base_config = {}
ebtel_interface = EbtelInterface({},DummyHeatingModel(),'','')

# calculate fractional ionization
field.calculate_fractional_ionization(emiss_model,interface=ebtel_interface,
                                      savefile=args.nei_save)

# save field
field.save(savedir=args.field_path)