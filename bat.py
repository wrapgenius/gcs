#!/usr/bin/env python

# Standard modules
import pdb
import os.path
import sys
import shutil
import time
import logging
import importlib
from lxml import html
import requests
import pyquery
import random
import pandas as pd
import numpy as np

# Modules within this package
from heatmap import heatmap_url
from heatmap import get_heatmap
from heatmap import predict_general_heatmap
import functions as fn
from player import Player

def main():
	first_name = sys.argv[1]
	last_name = sys.argv[2]

	path_data = '/Users/marco/Code/Python/Modules/gcs/data/'
	file_master_list = 'master_player_list.csv'
	plyr = Player(path_data + file_master_list)
	fg_id = plyr.get_fg_id(first_name=first_name,last_name=last_name)[0]
	print 'fangraphs_id '+ str(fg_id)

	ps = predict_general_heatmap(int(fg_id), 8, 'swing')
	if ps == True: 
		print 'swing!' 
		pc = predict_general_heatmap(int(fg_id), 8, 'contact' )
		#print pc
		if pc == True: print 'contact!' 
	else:
		cs = predict_general_heatmap(int(fg_id), 8, 'cStrike')
		if cs == True:
			print 'strike!'
		else:
			print 'ball!'

def predict_swing(fangraphs_id, pitch_placement, heatmap_type='swing', pitch_type='', hand='all', count='all', season='all'):
	'''
	Return a prediction based on pitch placement, and swing percentage.
	Not clear if should also predict type or outcome of a swing here or in a seperate function.
	'''
	url = heatmap_url(fangraphs_id, heatmap=heatmap_type, pitch=pitch_type, hand=hand, count=count, season=season)
	#print url
	heatmap = get_heatmap(url)

	#pdb.set_trace()
	# For starters the outcome is True/False
	if np.random.rand()*100. <= heatmap[pitch_placement]:
		swing = True
	else:
		swing = False

	return swing

def predict_outcome():
	'''
	False would be a foul ball out of play
	'''

	return False


if __name__=="__main__":
    main()
else:
    logging.info("Note: `pitch` module not being run as main executable.")