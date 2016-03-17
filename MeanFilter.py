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
			self.values.pop(0)
		self.values.append(val)
		
	def getMean(self):
		sum = 0
		for elem in self.values:
			sum = sum + elem
		print("lenght")
		print(len(self.values))
		return elem / len(self.values)
