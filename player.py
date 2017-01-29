'''
	Specific Player Information
'''
import pdb
from lxml import html
import requests
import pyquery
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

class Player:

    def __init__(self, file_master_list):
        
        players_list = pd.read_csv(file_master_list)
        full_names = [str(i).split() for i in players_list.fg_name.values]
        first_names = []
        last_names = []
        for i in range(len(full_names)):
            if full_names[i][0] != 'nan':
                first_names.append(full_names[i][0])
                last_names.append(full_names[i][1])
            else: 
                first_names.append('nan')        
                last_names.append('nan')
        players_list['first_name'] = first_names
        players_list['last_name'] = last_names
        
        self.master_list = players_list
        
    def get_mlb_id(self, full_name=None,first_name=None,last_name=None):
        if (full_name == None):
            mlb_id = self.master_list.mlb_id[(self.master_list.first_name.values == first_name) & 
                                                  (self.master_list.last_name.values == last_name)].values
        else:
            mlb_id = self.master_list.mlb_id[(master_list.mlb_name.values == full_name)]
        
        return mlb_id
        
    def get_fg_id(self, full_name=None,first_name=None,last_name=None):
        if (full_name == None):
            fangraphs_id = self.master_list.fg_id[(self.master_list.first_name.values == first_name) & 
                                                  (self.master_list.last_name.values == last_name)].values
        else:
            fangraphs_id = self.master_list.fg_id[(master_list.mlb_name.values == full_name)]
        
        return fangraphs_id
        
    def get_lahman_id(self, full_name=None,first_name=None,last_name=None):
        if (full_name == None):
            lahman_id = self.master_list.lahman_id[(self.master_list.first_name.values == first_name) & 
                                                  (self.master_list.last_name.values == last_name)].values
        else:
            lahman_id = self.master_list.lahman_id[(master_list.mlb_name.values == full_name)]
        
        return lahman_id
        
    def get_mlb_position(self, full_name=None,first_name=None,last_name=None):
        if (full_name == None):
            mlb_position = self.master_list.mlb_pos[(self.master_list.first_name.values == first_name) & 
                                                  (self.master_list.last_name.values == last_name)].values
        else:
            mlb_position = self.master_list.mlb_pos[(master_list.mlb_name.values == full_name)]
        
        return mlb_position

    def get_player_info_w_id(self,fangraphs_id, info = None):
        if (info == None):
            out = self.master_list[self.master_list.fg_id == fangraphs_id]
            return out
        else:
            out = self.master_list[info][self.master_list.fg_id == fangraphs_id]
            return out.values
        
    def get_player_info(self,info=None,full_name=None,first_name=None,last_name=None):
        #pdb.set_trace()
        if (full_name == None):
            tid = self.get_fg_id(first_name=first_name,last_name=last_name)
        else:
            tid = self.get_fg_id(full_name=full_name)
        return self.get_player_info_w_id(tid[0],info=info)[0]


