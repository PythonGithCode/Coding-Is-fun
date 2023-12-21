import logging
import random

logging.basicConfig(level=logging.DEBUG)

class PropertieBase:
	def __init__(self, **properties):
		super().__init__()
		Properties = self
		self.properties = properties
		self.rand = random.random()
	
	def getPropertie(self, Value):
		return self.properties[str(Value)]
	
	def setPropertie(self, Value, value):
		self.properties[str(Value)] = value
	
	def getRandom(self):
		return self.rand


# print(PropertieBase().getRandom())
# print(PropertieBase().getRandom())


# class Properties():
# 	# this is going to be used to added it to other classes
# 	properties = PropertieBase()

# 	def __init__(self):
# 		super().__init__()
# 		# properties = PropertieBase()




class StoreName:
	properties = PropertieBase()

	def __init__(self, Name, Count = 0, **properties):
		super().__init__()
		self.Name = Name
		self.Count = Count
	
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
		self.NameDict.update({storeName.getName(): storeName})
	
	def getName(self, nameValue):
		return self.NameDict[str(nameValue)]
	

NamesConstant = Names()

class dog(Names):
	properties = PropertieBase()
	
	def __init__(self, nameV=None, **properties):
		super().__init__()
		self.NameV = nameV
	
	def getName(self):
		return self.Name
	
	def setName(self, nameValue):
		# setdefualt name if the new name is a name that did't be there before
		return self.NameDict



NamesConstant.makeNewName("Dave")

print(NamesConstant.getNames())



Dave = dog("dave")

print(Dave.setName("ok"))
#print(Dave.Properties)

logging.info("dave props: %s", Dave.properties.getRandom())

logging.info("dave props2: %s", Dave.properties.getRandom())

logging.info("props: %s", Properties.properties.getRandom())

# Dave.Properties().setPropertie("nothing", 1)
# print(Dave.Properties().getRandom())
# print(Dave.Properties().getRandom())
# print(Dave.Properties().getPropertie("nothing"))


#dave = dog()
#dave.properties["age"] = 9
#dave.setPropertie("name", "dave")

#print(dave.getPropertie("name"))

#print("ok")


