#!/usr/bin/env python3
import sys
sys.path.append('osrsApiWrapper')
from grandexchange import GrandExchange
from osrsbox import items_api

def GETrabeableFilter(item):
	return item.tradeable_on_ge


class ItemDB(object):

	def __init__(self):
		self.all_db_items = items_api.load()
		self.defaultFilter = GETrabeableFilter

	def setDefaultFilter(self, newFilter):
		self.defaultFilter = newFilter
		
	def getMatchesByName(self, name):
		return self.getMatchesByFilter(lambda x: x.name == name and self.defaultFilter(x))
	
	def getMatchesByFilter(self, filter, alsoDefault = True):
		matches = Matches()
		for item in self.all_db_items:
			if filter(item) and (not alsoDefault or self.defaultFilter(item)):
				matches.append(item)
		return matches

	def getItemById(self, id):
		return Match(self.all_db_items[id])


class Matches(object):

	def __init__(self, items = None):
		self.matches = []
		if items is not None:
			assert type(items) == list
			for item in items:
				self.matches.append(Match(item))

	def append(self, item):
		self.matches.append(Match(item))

	def __len__(self):
		return len(self.matches)

	def __getitem__(self, i):
		return self.matches[i]

	def __iter__(self):
		return iter(self.matches)


class Match(object):

	def __init__(self, item):
		self.item = item
		self.price = None
		if self.item.tradeable_on_ge:
			self.price = int(GrandExchange.item(item.id).price())

	def getItem(self):
		return self.item

	def getPrice(self):
		return self.price
		
	def __str__(self):
		return '{item: ' + str(self.item) + ', price: ' + str(self.price) + '}'

