import os
import shutil
from shutil import copy
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--path', type=str)
parser.add_argument('--exceptions', type=str)
parser.add_argument('--source', type=str)
args = parser.parse_args()

path = args.path
excepted_models = []
source = args.source
source = source.replace('\\', '/')
if args.exceptions is not None:
    excepted_models = args.exceptions.split(' ')
zombie_models = ['beiliya.vmdl_c', 'aybb.vmdl_c', 'szz.vmdl_c', 'chris_walker.vmdl_c', 'zgjs.vmdl_c',
                 'zombie_xiaoao.vmdl_c', 'zombie_miwu.vmdl_c', 'zombie_frozen.vmdl_c', 'resident_zombie.vmdl_c',
                 'dyel.vmdl_c', 'lbjur.vmdl_c', '1.vmdl_c', '2.vmdl_c', '3.vmdl_c', '4.vmdl_c']
excepted_models = excepted_models + zombie_models

for root, dirs, files in os.walk(path):
    for file in files:
        if not file.endswith('.vmdl_c'):
            continue
        if '_arm' in file:
            continue
        is_excepted_models = False
        for model in excepted_models:
            if file == model:
                is_excepted_models = True
                continue
        if not is_excepted_models:
            os.remove(f'{root}/{file}')
            copy(source, f'{root}/{file}')