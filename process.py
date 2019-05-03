#!/usr/bin/env python3
from enum import Enum
from itemDB import ItemDB

class InputType(Enum):
	TIME = 0
	MONEY = 1
	ITEM = 2
	ITEMVAR = 3
	
	
class ProcessInput(object):

	def __init__(self, inputType, amount, itemId = None, itemFilter = None):
		self.inputType = inputType
		self.amount = amount
		self.itemId = itemId
		self.itemFilter = itemFilter
		if self.inputType is InputType.ITEM and itemId is None:
			raise ValueError
		if self.inputType is InputType.ITEMVAR and itemFilter is None:
			raise ValueError
			
	def getType(self):
		return self.inputType
		
	def getAmount(self):
		return self.amount
		
	def getItemId(self):
		return self.itemId
		
	def getItemFilter(self):
		return self.itemFilter
		
	
class OutputType(Enum):
	XP = 0
	MONEY = 1
	ITEM = 2
	ITEMVAR = 3
	ITEMFUNC = 4

	
class ProcessOutput(object):

	def __init__(self, outputType, amount, itemId = None, itemFilter = None, itemFunc = None, skill = None):
		self.outputType = outputType
		self.amount = amount
		self.itemId = itemId
		self.itemFilter = itemFilter
		self.itemFunc = itemFunc
		self.skill = None
		if self.outputType is OutputType.XP and self.skill is None:
			raise ValueError
		if self.outputType is OutputType.ITEM and itemId is None:
			raise ValueError
		if self.outputType is OutputType.ITEMVAR and itemFilter is None:
			raise ValueError
		if self.outputType is OutputType.ITEMFUNC and itemFunc is None:
			raise ValueError
	
	def getType(self):
		return self.inputType
		
	def getAmount(self):
		return self.amount
		
	def getItemId(self):
		return self.itemId
		
	def getItemFilter(self):
		return self.itemFilter
		
	def getItemFunc(self):
		return self.itemFunc
	
	
class SkillRequirement(object):

	def __init__(self, skill, level):
		self.skill = skill
		self.level = level
		
	def getSkill(self):
		return self.skill
		
	def getLevel(self):
		return self.level
	
	
class Process(object):

	Process.itemDB = ItemDB()

	def __init__(self, inputList, outputList, skillRequirements):
		self.inputs = inputList
		self.outputs = outputList
		self.skillReqs = skillRequirements