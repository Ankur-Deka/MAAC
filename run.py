# -------- import GridSearch and define/import the compile function -------- #
import sys
sys.path.append('SIGS-Grid-Search')
from grid_search import GridSearch


# -------- main file to run -------- #
mode = 'train' # train/test
num_process = 6

# -------- define dictionary of arguments for grid search -------- #
if mode == 'train':
	main_file = 'main.py'
	args = 	{
			# 'cpus': ['37,38,39,40,41'],
			'env_id': ['simple_spread'],
			'model_name': ['exp_1'],
			'n_episodes': [2000000],
			'save_interval': [2000],
			'use_gpu': ['']}
elif mode =='test':
	main_file = 'evaluate.py'
	args = {
			'env_id': ['simple_adversary'],
			'model_name': ['exp_1'],
			'run': [1],
			'incremental': [88009],
			'save_gifs': ['']
		   }


# -------- create GridSearch object and run -------- #
myGridSearch = GridSearch(main_file, args, num_process=num_process)
myGridSearch.run()
