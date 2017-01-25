'''
Embedded Classes containing Teams, Lineups, Players
'''

# Standard modules
import pdb
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

	def import_lineup_cfg(self,lineup_file_path):
		'''
		Turn .cfg file of player names into a roster lineup
		'''

		config = ConfigParser.SafeConfigParser()
		config.read(lineup_file_path)

		home = dict(config.items('home'))
		away = dict(config.items('away'))

		pdb.set_trace()

		home_lineup = {}
		lineup_position = 1
		for player in home:
			home_lineup[str(lineup_position)] = str(player)
			lineup_position += 1

		away_lineup = {}
		lineup_position = 1
		for player in home:
			away_lineup[str(lineup_position)] = str(player)
			lineup_position += 1


		self.roster['home'] = home_lineup
		self.roster['away'] = away_lineup


	def import_lineup_gameid(self,mlb_game_id):
		#eventually by mlb_game_id
		print 'soon!'
