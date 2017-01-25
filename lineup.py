'''
Embedded Classes containing Teams, Lineups, Players
'''

# Standard modules
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

class Team(main):
	def __init__():
		self.roster = {}

def import_lineup_cfg(lineup_file_path):
	'''
	Turn .cfg file of player names into a roster lineup
	'''

	config = ConfigParser.SafeConfigParser()
	config.read(lineup_file_path)

	home_lineup = dict(config.items('home'))
	visitor_lineup = dict(config.items('visitor'))



def import_lineup_gameid(mlb_game_id):
	#eventually by mlb_game_id
	print 'soon!'
