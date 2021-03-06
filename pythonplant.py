'''
Documentation, License etc.

@package pythonplant
'''

#!/usr/bin/env python2
# -*- coding: utf-8-*-

import serial
import re
from MeanFilter import *

class Plant(object):
	def __init__ (self):
		self.water = 0
		self.min_water = 300
		self.flag = True
		self.mean_plant = MeanFilter()

	def getWater(self):
		return self.mean_plant.getMean()
		
	def update(self, water_value):
		self.water = water_value
		self.mean_plant.addValue(water_value)
		
	def is_thirsty(self):
		if(self.mean_plant.getMean() < self.min_water):
			return True
		else:
			return False



def updateValue(ser, plant1, plant2):
	#print("reading")
	ser.flushInput()
	ser.readline()
	value = ser.readline()	
	print(value)
	splitted = value.split(":")
	#print(splitted)
	if(len(splitted) == 5):	
		plant1.update( int(splitted[1] ) );
		plant2.update( int(splitted[3] ) );
