#!/usr/bin/env python

# Standard modules
import pdb
import pandas as pd
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
import functions as fn
from player import Player

#testing solv

def main(): #fangraphs_id = None, pitch='', hand='all', count='all', season='2016'):
	#	if fangraphs_id == None:
	#	fangraphs_id = sys.argv
	first_name = sys.argv[1]
	last_name = sys.argv[2]

	path_data = '/Users/marco/Code/Python/Modules/gcs/data/'
	file_master_list = 'master_player_list.csv'
	plyr = Player(path_data + file_master_list)
	fg_id = plyr.get_fg_id(first_name=first_name,last_name=last_name)[0]
	#print int(fg_id)

	pt = predict_pitch_type(int(fg_id))
	print pt
	pv = predict_pitch_velocity(int(fg_id), pitch_type = pt)
	print pv
	pp = predict_pitch_placement(int(fg_id), pitch_type = pt)
	print pp

	return [int(fg_id), pt, pv, pp]

def predict_pitch_placement(fangraphs_id, pitch_type='', hand='all', count='all', season='all'):

	url = heatmap_url(fangraphs_id, position = 'P', pitch=pitch_type, hand=hand, count=count, season=season)
	#print url
	heatmap = get_heatmap(url)

	return fn.inverse_transform_sample(heatmap)

def predict_pitch_type(fangraphs_id):
	'''To start, figure out what pitches and what the rate is. Eventually, a Markov treatment'
	'''

	path = '/Users/marco/Code/Python/Modules/gcs/data/FanGraphs_Pitch_Type_2016.csv'
	player_pitch_types = pd.read_csv(path) # .fillna

	pitch_names = player_pitch_types.columns.values[3:17]
	#pdb.set_trace()
	pitch_freqs = player_pitch_types[(player_pitch_types.playerid == fangraphs_id)].values[0][3:17]
	y=np.array([float(str(x).split()[0]) for x in pitch_freqs])
	z=np.array([])
	for i in y:
		if i > 0:
			z = np.append(z,float(i))
		else:
			z = np.append(z,0.0)

	pitch_type = pitch_names[fn.inverse_transform_sample(z)].split('%')[0]

	return pitch_type

def predict_pitch_velocity(fangraphs_id, pitch_type, inning='all'):

	path = '/Users/marco/Code/Python/Modules/gcs/data/FanGraphs_Pitch_Velocity_2016.csv'
	player_pitch_types = pd.read_csv(path)

	pitch_column = np.where(player_pitch_types.columns.values == 'v'+pitch_type)[0][0]
	pitch_velocity   = player_pitch_types[player_pitch_types.playerid == fangraphs_id].values[0][pitch_column]

	return pitch_velocity + np.random.randn()*np.sqrt(pitch_velocity/15.)

if __name__=="__main__":
    main()
else:
    logging.info("Note: `pitch` module not being run as main executable.")
