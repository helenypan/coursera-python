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

class FootballFan(PartyAnimal):
	points = 0
	def touchdown(self):
		self.points = self.points + 7 
		self.party()
		print self.name, "ponts",self.points


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()