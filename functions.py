import numpy as np
import random



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
	# inverse transform sample the vector of probabilities
	# not necessary that sum of pdf = 1.
    pitch = False
    while pitch == False:
        location = random.randint(0,len(pdf)-1)
        prob = np.random.uniform(np.min(pdf),np.max(pdf))
        if prob < pdf[location]: pitch = True  
    return location
