import pdb
from lxml import html
import requests
import pyquery
import numpy as np
import pandas as pd
import random
import functions as fn

def heatmap_url(playerid='', position = '', heatmap='pitch', pitch='', start_date='', end_date='', hand='all', count='all', season=''):
    if playerid != '': playerid = str(playerid)
    if heatmap != 'pitch=': heatmap = fn.translate_type(heatmap)
    url0 = 'http://www.fangraphs.com/zonegridbase.aspx?'
    pid_suf  = 'playerid=' + str(playerid)+'&'
    pos_suf  = 'position='+position+'&'
    ss_suf   = 'ss='+start_date+'&' # Start Date - 2016-04-05 
    se_suf   = 'se='+end_date+'&' # End Date - 2016-08-02 
    type_suf = 'type='+heatmap+'&' # 
    hand_suf = 'hand='+str(hand)+'&'
    count_suf= 'count='+str(count)+'&' # 'ahead', 'behind', '0,1', '3,2', etc.
    blur_suf = 'blur=0&'
    grid_suf = 'grid=5&'
    view_suf = 'view=bat&'
    pitch_suf= 'pitch='+pitch+'&' # CH CU FA FC FT SL 
    season_suf= 'season='+str(season)

    url=url0+pid_suf+pos_suf+ss_suf+se_suf+type_suf+hand_suf+count_suf+blur_suf+grid_suf+view_suf+pitch_suf+season_suf
    
    return url

def get_heatmap(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    heats = tree.xpath('//div[@class="hzstat"]/text()')
    Npitch = tree.xpath('//div[@class="hzdem"]/text()')
    heat1d = [float(i.split()[0]) for i in heats]
    Npitch1d = [float(i.split()[0]) for i in Npitch]

    return heat1d

def predict_general_heatmap(fangraphs_id, pitch_placement, heatmap_type, pitch_type='', hand='all', count='all', season='all'):
    '''
    Generalized function returns a True/False prediction based on pitch placement, and field percentage.
    '''
    url = heatmap_url(fangraphs_id, heatmap=heatmap_type, pitch=pitch_type, hand=hand, count=count, season=season)
    #print url
    heatmap = get_heatmap(url)

    #pdb.set_trace()
    # For starters the outcome is True/False
    print heatmap_type +'='+str(heatmap[pitch_placement])
    if np.random.rand()*100. <= heatmap[pitch_placement]:
        outcome = True
    else:
        outcome = False

    return outcome

def translate_type(input_type):
    if input_type.lower() == 'pitch':  #pitch%
        return '0'
    if input_type.lower() == 'strike': #strike%
        #print 'strike %!'
        return '1'
    if input_type.lower() == 'swing':  #swing%
        return '2'
    if input_type.lower() == 'contact':#contact%
        return '3'
    if input_type.lower() == 'avg' or input_type.lower() == 'avg/p':
        return '4'
    if input_type.lower() == 'slg' or input_type.lower() == 'slg/p':
        return '5'
    if input_type.lower() == 'iso' or input_type.lower() == 'iso/p':
        return '6'
    if input_type.lower() == 'raa' or input_type.lower() == 'raa/p' or input_type.lower() == 'raa/100p':
        return '7'
    if input_type.lower() == 'gb' or input_type.lower() == 'gb/p':
        return '8'
    if input_type.lower() == 'cstrike' or input_type.lower() == 'called_strike':
        return '9'
    else:
        return input_type
