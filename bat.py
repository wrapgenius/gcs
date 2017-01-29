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

def batting_heatmap_url(playerid, pitch='', hand='all', count='all', season='all'):
	#E.g Mookie Betts:
	#http://www.fangraphs.com/zonegrid.aspx?playerid=13611&position=&ss=2016-04-05&se=2016-10-02&type=0&hand=R&count=all&blur=0&grid=5&view=bat&pitch=&season=all
    url0 = 'http://www.fangraphs.com/zonegrid.aspx?'
    pid_suf  = 'playerid=' + str(playerid)+'&'
    pos_suf  = 'position=&'
    ss_suf   = 'ss=&' # Start Date - 2016-04-05 
    se_suf   = 'se=&' # End Date   - 2016-08-02 
    type_suf = 'type=0&'
    hand_suf = 'hand='+str(hand)+'&'
    count_suf= 'count='+str(count)+'&' # 'ahead', 'behind', '0,1', '3,2', etc.
    blur_suf = 'blur=0&'
    grid_suf = 'grid=5&'
    view_suf = 'view=bat&'
    pitch_suf= 'pitch='+pitch+'&'
    season_suf= 'season='+str(season)
    
    url=url0+pid_suf+pos_suf+ss_suf+se_suf+type_suf+hand_suf+count_suf+blur_suf+grid_suf+view_suf+pitch_suf+season_suf
    
    return url

def format_date(input_date):
	print 'will eventually take any date format and return str(YYYY-MM-DD)'

def translate_type(input_type):
	if input_type.lower() == 'pitch':
		return 0
	if input_type.lower() == 'strike':
		return 0
	if input_type.lower() == 'swing':
		return 0
	if input_type.lower() == 'contact':
		return 0
	if input_type.lower() == 'slg' or input_type.lower() == 'slg/p':
		return 0
	if input_type.lower() == 'iso' or input_type.lower() == 'iso/p':
		return 0
	if input_type.lower() == 'raa' or input_type.lower() == 'raa/p' or input_type.lower() == 'raa/100p':
		return 0
	if input_type.lower() == 'gb' or input_type.lower() == 'gb/p':
		return 0
	if input_type.lower() == 'cstrike' or input_type.lower() == 'strike':
		return 0
