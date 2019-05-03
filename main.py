#!/usr/bin/env python3
import sys
sys.path.append('osrsApiWrapper')
from hiscores import Hiscores
from itemDB import ItemDB

def printMatches(itemDB, filter):
	for match in itemDB.getMatchesByFilter(filter):
		print (match.getItem().name, match.getPrice())

def stringableFilter(item):
	name = item.name.lower()
	if 'amulet (u)' in name:
		return True
	if 'unstrung' in name and 'bow' not in name and 'ballista' not in name:
		return True
	return False

if __name__ == "__main__":
	myName = '10denver10'
	# myHiscores = Hiscores(myName)
	# for k, v in myHiscores.skills.items():
		# print(k,v)
		
	# print(myHiscores.skills['magic'].level)
	# print(myHiscores.skills['magic'].xp_tnl())
	# print(myHiscores.max_skill().name)
	
	items = ItemDB()
	
	# whip_id = 4151
	# whip = items.getItemById(whip_id)
	# print(whip)
	
	# runes = items.getMatchesByName('Nature rune')
	# print(runes)
	# for item in runes:
		# print(item)
		
	# amulets = items.getMatchesByFilter(lambda item: 'amulet' in item.name.lower())
	# for match in amulets:
		# print(match.getItem().name, match.getPrice())
		
	printMatches(items, stringableFilter)
	# print()
	# printMatches(items, lambda item: 'holy' in item.name.lower())