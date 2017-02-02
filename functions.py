import numpy as np
import random

def batter_count(count_in, heatmap_position, heatmap_style = '5x5'):

	return count_out

def clean_nans(dirty_array, replacement_char=0.0):
	clean_array = dirty_array
	clean_array[np.isnan(dirty_array)] = replacement_char
	clean_array[np.isinf(dirty_array)] = replacement_char

def format_date(input_date):
	print 'will eventually take any date format and return str(YYYY-MM-DD)'
	formatted_date = '2016-06-14'
	return formatted_date

def inverse_transform_sample(pdf):
	#def predict_pitch_location(heatmap):
	# inverse transform sample the heatmap
    pitch = False
    while pitch == False:
        location = random.randint(0,len(pdf)-1)
        prob = np.random.uniform(np.min(pdf),np.max(pdf))
        if prob < pdf[location]: pitch = True  
    return location

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
    if input_type.lower() == 'cstrike' or input_type.lower() == 'strike':
        return '9'
    else:
        return input_type