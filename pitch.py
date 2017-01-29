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
#import functions as fn
#import parameters # Changed from "import parameters"
import heatmap
import player

#This will eventually be read from the lineup parameter file
#path_data = '/Users/marco/Code/Python/Modules/gcs/data/'
#file_master_list = 'master_player_list.csv'

#def main(fangraphs_id = None, pitch='', hand='all', count='all', season='2016'):
#	if fangraphs_id == None:
#		fangraphs_id = sys.argv
def predict_pitch_placement(fangraphs_id, pitch='', hand='all', count='all', season='all'):

	url = pitch_heatmap_url(fangraphs_id, pitch=pitch, hand=hand, count=count, season=season)
	heatmap = get_heatmap(url)

	return inverse_transform_sample(heatmap)

def predict_pitch_type():
	print 'To start, figure out what pitches and what the rate is. Eventually, a Markov treatment'

	return pitch_type
def get_heatmap(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	heats = tree.xpath('//div[@class="hzstat"]/text()')
	Npitch = tree.xpath('//div[@class="hzdem"]/text()')
	heat1d = [float(i.split()[0]) for i in heats]
	Npitch1d = [float(i.split()[0]) for i in Npitch]

	return heat1d

def inverse_transform_sample(heatmap):
    pitch = False
    while pitch == False:
        location = random.randint(0,len(heatmap)-1)
        prob = np.random.uniform(np.min(heatmap),np.max(heatmap))
        if prob < heatmap[location]: pitch = True  
    return location

def pitch_heatmap_url(playerid, pitch='', hand='all', count='all', season='2016'):
    url0 = 'http://www.fangraphs.com/zonegrid.aspx?'
    pid_suf  = 'playerid=' + str(playerid)+'&'
    pos_suf  = 'position=P&'
    ss_suf   = 'ss=&' # Start Date - 2016-04-05 
    se_suf   = 'se=&' # End Date - 2016-08-02 
    type_suf = 'type=0&'
    hand_suf = 'hand='+str(hand)+'&'
    count_suf= 'count='+str(count)+'&' # 'ahead', 'behind', '0,1', '3,2', etc.
    blur_suf = 'blur=0&'
    grid_suf = 'grid=5&'
    view_suf = 'view=bat&'
    pitch_suf= 'pitch='+pitch+'&' # CH CU FA FC FT SL 
    season_suf= 'season='+str(season)
    
    url=url0+pid_suf+pos_suf+ss_suf+se_suf+type_suf+hand_suf+count_suf+blur_suf+grid_suf+view_suf+pitch_suf+season_suf
    
    return url

def translate_pitch(input_pitch):
	if input_pitch.lower() == 'pitch':
		return 0
	if input_pitch.lower() == 'strike':
		return 0
	if input_pitch.lower() == 'swing':
		return 0
	if input_pitch.lower() == 'contact':
		return 0
	if input_pitch.lower() == 'slg' or input_pitch.lower() == 'slg/p':
		return 0
	if input_pitch.lower() == 'iso' or input_pitch.lower() == 'iso/p':
		return 0
	if input_pitch.lower() == 'raa' or input_pitch.lower() == 'raa/p' or input_type.lower() == 'raa/100p':
		return 0
	if input_pitch.lower() == 'gb' or input_pitch.lower() == 'gb/p':
		return 0
	if input_pitch.lower() == 'cstrike' or input_pitch.lower() == 'strike':
		return 0

if __name__=="__main__":
    main()
else:
    logging.info("Note: `pitch` module not being run as main executable.")