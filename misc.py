import os

outs_folder = 'outs'
outs_files = os.listdir(outs_folder)
start = 1

def get_next_filename(cat):
	cat_files = [f for f in outs_files if cat in f]
	idx = max([int(f.split('.')[0].split('_')[1]) for f in cat_files]) + 1
	return f'{outs_folder}/{cat}_{idx}.csv'