#!/home/vossj/suncat/bin/python

#SBATCH -p dev
#SBATCH --job-name=opt.py
#SBATCH --output=myjob.out
#SBATCH --error=myjob.err
#SBATCH --time=1:00:00                                 #default is 20 hours
#SBATCH --nodes=1
##SBATCH --mem-per-cpu=4000
#SBATCH --mail-type=END,FAIL                            #get emailed about job BEGIN, END, or FAIL
#SBATCH --mail-user=allegralatimer@gmail.com
##SBATCH --ntasks-per-node=16                            #task to run per node; each node has 16 cores

import catmap
import numpy as np
import os
from catmap import ReactionModel
from catmap import analyze
from matplotlib import pyplot as plt

#mkm_file = [f for f in os.listdir('.') if f.endswith('.mkm')][0]
model = ReactionModel(setup_file='mechanism.mkm')
model.output_variables.append('production_rate')
model.output_variables.append('free_energy')
#model.output_variables.append('interaction_matrix')
model.run()

vm = analyze.VectorMap(model)
vm.model_name = 'CH3OH'
vm.plot_variable = 'free_energy'
vm.log_scale = False
vm.plot(save=vm.plot_variable+'.pdf')

vm.plot_variable = 'coverage'
vm.min = 0
vm.max = 1
vm.plot(save=vm.plot_variable+'.pdf')

vm.plot_variable = 'production_rate'
vm.log_scale = True
vm.min = 1e-25
vm.max = 1e3
vm.include_labels = ['CH3OH_g']
vm.descriptor_labels = ['E_C [eV]', 'E_O [eV]']
vm.subplots_adjust_kwargs = {'left':0.2,'right':0.8,'bottom':0.15}
fig = vm.plot(save='CH3OH_g.pdf')
#fig.set_figwidth(10)
#fig.set_figheight(10)
#fig.savefig('production_rate.pdf')

vm.plot_variable = 'production_rate'
vm.log_scale = True
vm.min = 1e-25
vm.max = 1e3
vm.include_labels = ['CH2O_g']
vm.descriptor_labels = ['E_C [eV]', 'E_O [eV]']
vm.subplots_adjust_kwargs = {'left':0.2,'right':0.8,'bottom':0.15}
fig = vm.plot(save='CH2O_g.pdf')

vm.plot_variable = 'production_rate'
vm.log_scale = True
vm.min = 1e-25
vm.max = 1e3
vm.include_labels = ['CO_g']
vm.descriptor_labels = ['E_C [eV]', 'E_O [eV]']
vm.subplots_adjust_kwargs = {'left':0.2,'right':0.8,'bottom':0.15}
fig = vm.plot(save='CO_g.pdf')

vm.plot_variable = 'production_rate'
vm.log_scale = True
vm.min = 1e-25
vm.max = 1e3
vm.include_labels = ['CO2_g']
vm.descriptor_labels = ['E_C [eV]', 'E_O [eV]']
vm.subplots_adjust_kwargs = {'left':0.2,'right':0.8,'bottom':0.15}
fig = vm.plot(save='CO2_g.pdf')










sa = analyze.ScalingAnalysis(model)
sa.plot(save='scaling.pdf')





