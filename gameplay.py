#!/usr/bin/env python

'''
	Main Game organization
'''

# Standard modules
import pdb
import pandas as pd
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
from heatmap import heatmap_url
from heatmap import get_heatmap
import functions as fn
from player import Player

#import parameters #

#This will eventually be read from the lineup parameter file
#path_data = '/Users/marco/Code/Python/Modules/gcs/data/'
#file_master_list = 'master_player_list.csv'



if __name__=="__main__":
    main()
else:
    logging.info("Note: `pitch` module not being run as main executable.")