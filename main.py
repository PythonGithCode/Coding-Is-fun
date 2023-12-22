import logging
import random

logging.basicConfig(level=logging.DEBUG)

class PropertieBase:
	def __init__(self, **properties):
		super().__init__()
		self.properties = properties
		self.rand = random.random()
	
	def gets(self, Value):
		return self.properties[str(Value)]
	
	def sets(self, Value, value):
		self.properties[str(Value)] = value
	
	def getR(self):
		return self.rand



class StoreName:
	properties = PropertieBase()

	def __init__(self, Name, Count = 0, **properties):
		super().__init__()
		self.Name = Name
		self.Count = Count
	
	def __str__(self):
		return str(self.Name) + ", " + str(self.Count)
	
	def add(self):
		self.Count += 1
	
	def getName(self):
		return self.Name
	
	def getCount(self):
		return self.Count



class Names():
	properties = PropertieBase()

	def __init__(self, NameDict={}, **properties):
		super().__init__()
		self.NameDict  = NameDict
	
	def makeNewName(self, nameValue, countValue=1):
		self.NameDict.update({str(nameValue): StoreName(nameValue, countValue)})
	
	def getNames(self):
		return self.NameDict.keys()
	
	def addName(self, storeName):
		if type(storeName) != type(StoreName):
			StoreName = StoreName(storeName, 1)
		self.NameDict.update({storeName.getName(): storeName})
	
	def getName(self, nameValue):
		return self.NameDict[str(nameValue)]
	

NamesConstant = Names()

class dog(Names):
	properties = PropertieBase()

	def __init__(self, nameV=None, **properties):
		super().__init__()
		self.NameV = nameV
		NamesConstant.addName(self.NameV)
	
	def getName(self):
		return self.Name
	
	def setName(self, nameValue):
		# setdefualt name if the new name is a name that did't be there before
		return self.NameDict



NamesConstant.makeNewName("dave")

print(NamesConstant.getNames())



Dave = dog("dave")

print(Dave.setName("ok"))
#print(Dave.Properties)

logging.info("dave props: %s", Dave.properties.getR())

logging.info("dave props2: %s", Dave.properties.getR())

logging.info("Name props2: %s", NamesConstant.properties.getR())

logging.info("Name Dave: %s", NamesConstant.getName("dave"))




