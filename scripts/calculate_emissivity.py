import os

from synthesizAR.atomic import EmissionModel

ar_root = '/data/datadrive1/ar_forward_modeling/systematic_ar_study'

emission_model = EmissionModel.restore(os.path.join(ar_root,'emission_model1109'))

emission_model.calculate_emissivity()

emission_model.save(savedir=os.path.join(ar_root,'emission_model1109'))