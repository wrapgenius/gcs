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
from player import Player_Profile

class Team:

	def __init__(self):
		self.roster = {}
		self.stats = {}

	def import_lineup_cfg(self,lineup_file_path):
		'''
		Turn .cfg file of player names into a roster lineup
		'''

		config = ConfigParser.SafeConfigParser()
		config.read(lineup_file_path)

		path = dict(config.items('player_info'))

		self.file_master_list = path['path_data'] + path['file_master_list']

		home = dict(config.items('home'))
		away = dict(config.items('away'))

		home_lineup = [] 
		away_lineup = [] 

		for i in range(len(home)):
			home_lineup.append(home['b'+str(i+1)])
			away_lineup.append(away['b'+str(i+1)])

		self.roster['home'] = home_lineup
		self.roster['away'] = away_lineup


	def import_lineup_gameid(self,mlb_game_id):
		#eventually by mlb_game_id
		print 'soon!'

	def get_players_info(self,first_name=None,last_name=None):
		players = Player_Profile(self.file_master_list)
		#self.roster
