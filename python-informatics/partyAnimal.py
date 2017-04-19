class PartyAnimal:
	x = 0 
	name = ""

	def __init__(self, name):
		self.name = name
		print "I am constructed", self.x, self.name

	def party(self):
		self.x = self.x + 1
		print self.name, "So far", self.x

	def __del__(self):
		print "I am destructed", self.name, self.x

an = PartyAnimal("Helen")
an.party()
an.party()
an.party()

ab = PartyAnimal("Wudong")
ab.party()
ab.party()

# print "Type", type(an)
# print "Dir",dir(an)