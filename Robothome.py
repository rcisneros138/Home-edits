import random
from msvcrt import getch
class PowerSupply:
	def __init__ (self, power = 100):
		self.power = power
	def displayPowerRemaining (self):
		print "Power remaining: ", self.power
	def charge(self, amount, power = 1000):
		if self.power < power:
			self.power = self.power + amount
			print "RoboCop charged +", amount
		else:
			raise Exception()
	def deplete(self, amount = 0):
		self.power = self.power - amount
		
		
class Stats:
	def __init__(self):
		self.bodyCount = 0
	def addBody(self, numOfBodies):
		self.bodyCount += numOfBodies
	def displayBodyCount(self):
		print "RoboCop has un-instanciated ", self.bodyCount, "criminals"
		
		
		
class Legs:
	def run(self, powerSupply):
		powerSupply.deplete(2)
		print "*RoboCop Runs*"
	def walk(self, powerSupply):
		powerSupply.deplete(1)
		print "*RoboCop Walks*"
	def roundHouse(self, powerSupply, stats):
		powerSupply.power = powerSupply.power - 5
		numOfHits = random.randrange(1, 5)
		stats.addBody(numOfHits)
		print "*RoboCop roundhouses", numOfHits, " criminal(s)* *Smack!!!!!*"
		
class Arms:
	def punch(self, powerSupply):
		powerSupply.deplete(4)
		print "*RoboCop punches the criminal*  *POWWW*"
	def shoot(self, powerSupply):
		powerSupply.deplete(3)
		hitChance = random.random()
		if (hitChance > .20):
			print "*RoboCop Shoots the criminal* *BANG*"
		else:
			print "Miss"
	def handcuff(self, powerSupply):
		powerSupply.deplete(2)
		print "*RoboCop handcuffs the criminal* Justice!!!"
		
class RightArm(Arms):
	def shoot(self,powerSupply):
		super (RightArm, self).shoot(powerSupply)
		hitChance = random.random()
		if (hitChance > .70):
			print "Right Arm bonus shot. Sweet!"
		
class Vision:
	def identifyCriminal(self, powerSupply):
		powerSupply.deplete(1)
		print "*Identifying criminal*"
	def targetCriminal(self, powerSupply):
		powerSupply.deplete(1)
		targetChance = random.random()
		if (targetChance > .25):
			print "*Criminal targeted.*"
		else:
			print "*Unable to target. Try again*"
		
class Speech:
	def yellHalt (self,powerSupply):
		powerSupply.deplete(1)
		print "*RoboCop yells 'HALT!'"
	def readRights (self, powerSupply):
		powerSupply.deplete(5)
		print "*RoboCop reads to suspect their rights with intense enthusiasm*"
	def mutterNoises (self, powerSupply):
		powerSupply.charge(2)
		print "*RoboCop shakes violently while muttering robot noises, giving +2 charge to his battery power"
		
class Test:
	def testLegs(self):
		legs = Legs()
		powerSupply.displayPowerRemaining()
		legs.run(powerSupply)
		powerSupply.displayPowerRemaining()
		legs.walk(powerSupply)
		powerSupply.displayPowerRemaining()
		legs.roundHouse(powerSupply)
		powerSupply.displayPowerRemaining()
	def testArms(self):
		arms = Arms()
		powerSupply.displayPowerRemaining()
		arms.punch(powerSupply)
		powerSupply.displayPowerRemaining()
		arms.shoot(powerSupply)
		powerSupply.displayPowerRemaining()
		arms.handcuff(powerSupply)
		powerSupply.displayPowerRemaining()
	def testVision(self):
		vision = Vision()
		powerSupply.displayPowerRemaining()
		vision.identifyCriminal(powerSupply)
		powerSupply.displayPowerRemaining()
		vision.targetCriminal(powerSupply)
	def testSpeech(self):
		speech = Speech()
		powerSupply.displayPowerRemaining()
		speech.yellHalt(powerSupply)
		powerSupply.displayPowerRemaining()
		speech.readRights(powerSupply)
		powerSupply.displayPowerRemaining()
		speech.mutterNoises(powerSupply)
		powerSupply.displayPowerRemaining()
		
class Controller:
	def roboCopController(self, powerSupply):
		while True:
			try:
				if powerSupply.power < 0:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
					key = ord(getch())
					if key == 27:
						break
					elif key == 113:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 119:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 104:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 112:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 115:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 99:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 100:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 97:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 116:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 98:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 101:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key == 102:
						speech.mutterNoises(powerSupply)
					elif key == 103:
						powerSupply.charge(10)
					elif key == 105:
						stats.displayBodyCount()
				else:
					key = ord(getch())
					if key == 27:
						break
					elif key == 113:
						legs.run(powerSupply)
					elif key == 119:
						legs.walk(powerSupply)
					elif key == 104:
						legs.roundHouse(powerSupply, stats)
					elif key == 112:
						arms.punch(powerSupply)
					elif key == 115:
						arms.shoot(powerSupply)
					elif key == 99:
						arms.handcuff(powerSupply)
					elif key == 100:
						powerSupply.displayPowerRemaining()
					elif key == 97:
						vision.identifyCriminal(powerSupply)
					elif key == 116:
						vision.targetCriminal(powerSupply)
					elif key == 98:
						speech.yellHalt(powerSupply)
					elif key == 101:
						speech.readRights(powerSupply)
					elif key == 102:
						speech.mutterNoises(powerSupply)
					elif key == 103:
						powerSupply.charge(10)
					elif key == 105:
						stats.displayBodyCount()
			except Exception:
				print "Max power reached"

powerSupply = PowerSupply()
legs = Legs()
arms = Arms()
vision = Vision()
speech = Speech()
test = Test()
stats = Stats()
# test = Test()
# test.testLegs()
# test.testArms()
#test.testVision()
# test.testSpeech()
controller = Controller()
controller.roboCopController(powerSupply)