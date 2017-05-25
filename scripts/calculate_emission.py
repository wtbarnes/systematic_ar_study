import os
import argparse

import synthesizAR
from synthesizAR.model_ext import EbtelInterface
from synthesizAR.atomic import EmissionModel


parser = argparse.ArgumentParser()
parser.add_argument("-e","--em_model_path",help="path to emission model")
parser.add_argument("-f","--field_path",help="path to field")
parser.add_argument("-m","--emiss_save",help="file to save emission results in")
args = parser.parse_args()

# restore field and emission model
field = synthesizAR.Skeleton.restore(args.field_path)
emiss_model = EmissionModel.restore(args.em_model_path)

# calculate fractional ionization
field.calculate_emission(emiss_model,savefile=args.emiss_save)

# save field
field.save(savedir=args.field_path)