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
field = synthesizAR.Skeleton.restore(args.field_path)
emiss_model = EmissionModel.restore(args.em_model_path, load_emissivity=False)

#create dummy ebtel interface for calculating NEI populations
class DummyHeatingModel(object):
    def __init__(self):
        self.base_config = {}
ebtel_interface = EbtelInterface({},DummyHeatingModel(),'','')

# configure options for nei calculation
ion_data_options = {'logTa':4.5,'logTb':8.0,'dlogT':0.05}
nei_solver_options = {'cutoff':1e-6}

# calculate fractional ionization
field.calculate_fractional_ionization(emiss_model,interface=ebtel_interface,
                                      savefile=args.nei_save,
                                      nei_solver_options=nei_solver_options,
                                      ion_data_options=ion_data_options
                                     )

# save field
field.save(savedir=args.field_path)