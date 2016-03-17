'''
Documentation, License etc.

@package pythonplant
'''

#!/usr/bin/env python2
# -*- coding: utf-8-*-

class MeanFilter(object):
	def __init__(self):
		self.values = list()
		#Using the last two minutes measurements
		self.max = 120
		
	def addValue(self, val):
		if(len(self.values) +1 > self.max):
			#print("pop")
			self.values.pop(0)
		self.values.append(val)
		
	def getMean(self):
		#print("getmean")
		sum = 0
		for elem in self.values:
			#print("elem")
			#print(elem)	
			sum = sum + elem
		#print("lenght")
		#print(len(self.values))
		#print(elem)
		if(len(self.values) > 0 ):
			return sum / len(self.values)
		else:
			return 0
