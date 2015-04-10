import time

class Cnt():
	def __init__(self):
		self.money = 0
		self.broken = False
	def getCoin(self, x ):
		print "przyjeto monete " + str(x)
		print "stan konta " + str(self.money + x)
		time.sleep(0.5)
		#sprawdza czy otrzymal monete i jesli tak to 
		#dodaje jej nominal do ilosci pieniedzy
		if (x > 0):
			self.money = self.money + x
		else:
			self.broken = True
	def isFull(self):
		if(self.money>4):
			self.money = 0
			return True
		else:
			return False

	def isBroken(self):
		if(self.broken):
			print "zepsuta"
			sys.exit()
