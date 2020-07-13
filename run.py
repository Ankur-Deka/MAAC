# -------- import GridSearch and define/import the compile function -------- #
import sys
sys.path.append('SIGS-Grid-Search')
from grid_search import GridSearch

# -------- main file to run -------- #
main_file = 'main.py'
num_process = 6

# -------- define dictionary of arguments for grid search -------- #
args = 	       {'cpus': [37,38,39,40,41],
		'env_id': ['simple_adversary'],
		'model_name': ['exp_1'],
		'n_episodes': [2000000],
		'save_interval': [2000],
		# 'cpus': ['37,38,39,40,41'],
		'cpus': ['42,43,44,45,46'],
		'use_gpu': ['']}

# -------- create GridSearch object and run -------- #
myGridSearch = GridSearch(main_file, args, num_process=num_process)
myGridSearch.run()
