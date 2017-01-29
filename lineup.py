'''
Embedded Classes containing Teams, Lineups, Players
'''

# Standard modules
import pdb
import numpy as np
import ConfigParser
import os
import os.path
import sys
import shutil
import time
import importlib
import logging
import pprint
from player import Player

class Team:

	def __init__(self, lineup_file_path):
		self.lineup = []
		self.roster = {}
		#self.stats = {}

		self.import_lineup_cfg(lineup_file_path)
		self.info = self.get_players_info() 

	def import_lineup_cfg(self,lineup_file_path):
		'''
		Turn .cfg file of player names into a roster lineup
		'''

		config = ConfigParser.SafeConfigParser()
		config.read(lineup_file_path)

		path = dict(config.items('player_info'))

		self.file_master_list = path['path_data'] + path['file_master_list']

		team = dict(config.items('player_names'))

		lineup = [] 
		for i in range(len(team)):
			lineup.append(team['b'+str(i+1)])

		self.lineup = lineup

	def import_lineup_gameid(self,mlb_game_id):
		#eventually by mlb_game_id
		print 'soon!'

	def get_players_info(self): #,first_name=None,last_name=None):

		all_players = Player(self.file_master_list)
		info = {}
		for iplayer in self.lineup:
			player = {}
			first_name = iplayer.split()[0]
			last_name = iplayer.split()[1]

			player['mlb_id']    = int(all_players.get_mlb_id(first_name=first_name,last_name=last_name)[0]) 
			player['fg_id']     = int(all_players.get_fg_id(first_name=first_name,last_name=last_name)[0]) 
			player['lahman_id'] = all_players.get_lahman_id(first_name=first_name,last_name=last_name)[0]
			player['position']  = all_players.get_mlb_position(first_name=first_name,last_name=last_name)[0] 

			info[iplayer] = player

		return info 
