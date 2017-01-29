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
path_data = '../data/'
file_master_list = 'master_player_list.csv'

def predict_pitch_placement(fangraphs_id, pitch='', hand='all', count='all', season='2016'):

	url = pitch_heatmap_url(fangraphs_id, pitch=pitch, hand=hand, count=count, season=season)
	heatmap = get_heatmap(url)

	return inverse_transform_sample(heatmap)

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
    ss_suf   = 'ss=&se=&'
    type_suf = 'type=0&'
    hand_suf = 'hand='+str(hand)+'&'
    count_suf= 'count='+str(count)+'&'
    blur_suf = 'blur=0&'
    grid_suf = 'grid=5&'
    view_suf = 'view=pit&'
    pitch_suf= 'pitch='+pitch+'&'
    season_suf= 'season='+str(season)
    
    url=url0+pid_suf+pos_suf+ss_suf+type_suf+hand_suf+count_suf+blur_suf+grid_suf+view_suf+pitch_suf+season_suf
    
    return url

if __name__=="__main__":
    main()
else:
    logging.info("Note: `pitch` module not being run as main executable.")