import pdb
from lxml import html
import requests
import pyquery
import numpy as np
import pandas as pd
import random

def pitch_heatmap_url(playerid, info=0, pitch='', hand='all', count='all', season='2016'):
    url0 = 'http://www.fangraphs.com/zonegrid.aspx?'
    pid_suf  = 'playerid=' + str(playerid)+'&'
    pos_suf  = 'position=P&'
    ss_suf   = 'ss=&se=&'
    type_suf = 'type='+str(info)+'&' # 0-Pitch% 1-Strike% 2-Swing% 3-Contact% 4-AVG 5-SLG 6-ISO 7-RAA/100 8-GB/P 9-cStrike%
    hand_suf = 'hand='+str(hand)+'&'
    count_suf= 'count='+str(count)+'&'
    blur_suf = 'blur=0&'
    grid_suf = 'grid=5&'
    view_suf = 'view=pit&'
    pitch_suf= 'pitch='+pitch+'&' #''-all 'CH'-Changeup 'CU'-Cutter 'FA'-4seam 'FC'-? 'FT' 'SL'-Slider
    season_suf= 'season='+str(season)
    
    url=url0+pid_suf+pos_suf+ss_suf+type_suf+hand_suf+count_suf+blur_suf+grid_suf+view_suf+pitch_suf+season_suf
    
    return url

def pitch_heatmap(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    heats = tree.xpath('//div[@class="hzstat"]/text()')
    Npitch = tree.xpath('//div[@class="hzdem"]/text()')
    heat1d = [float(i.split()[0]) for i in heats]
    rate1d = [float(i.split()[0]) for i in Npitch]
    #need to do some magic for cases with less than 25 entries!

    return heat1d, rate1d

def predict_pitch_location(heatmap):
    pitch = False
    while pitch == False:
        location = random.randint(0,len(heatmap)-1)
        prob = np.random.uniform(np.min(heatmap),np.max(heatmap))
        if prob < heatmap[location]: pitch = True  
    return location