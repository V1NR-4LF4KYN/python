'''
System for registering e.g. people with personal IDs

'''

# imports

# vars
areas = ["Bay Area"]
visitors = [0] # list of visitor's CIDs // CID 0 --> Placeholder.. starting visitors with 1

# classes
class Visitor:
	def __init__(self, cid, name, age, height, area):
		# Init Func for Visitors #
		self.cid = cid
		self.name = name
		self.age = age
		self.height = height
		self.area = area

	# getters
	def getCId(self):
		return self.cid

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

	def getHeight(self):
		return self.height

	def getArea(self):
		return self.area


	# setters
	def setCId(self, pId):
		self.cid = pId

	def setName(self, pName):
		self.name = pName

	def setAge(self, pAge):
		self.age = pAge

	def setHeight(self, pHeight):
		self.height = pHeight

	def setArea(self, pArea):
		self.area = pArea

	def getVisitors(self):
		global visitors
		print(visitors)


	# funcs for Visitors
	def getNextCId(self):
		global visitors
		self.nextCId = max(visitors) + 1
		return self.nextCId

	def addVstorToLst(self):
		global visitors

		self.setCId(self.getNextCId())
		visitors.append(self.cid)


	#TODO: add func for getting visitors name from cid...



# main
def main():
	global visitors

	print("Visitors before doing anything: {0}".format(visitors))
	jeff = Visitor(0, "Jeff", 24, 176, "Bay Area")
	jeff.addVstorToLst() # adding jeffs cid
	print("Visitors after adding Jeff: {0}".format(visitors))

	tim = Visitor(0, "Tim", 23, 182, "Bay Area")
	tim.addVstorToLst() # adding tims cid

	print("Visitors after adding Tim: {0}".format(visitors))

	print(visitors[1])


# calling main-loop
main()
print("")
