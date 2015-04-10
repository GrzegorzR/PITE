import time

class G():
	def __init__(self):
		self.state = "close"
		self.time = 0
	def openit(self):
		#otwiera bramke na 10 jednostek czasu
		print "bramka otwarta"
		self.state = "open"
		self.time = 10
	def close(self):
		#zamyka bramke
		print "bramka zamknieta"
		self.state = "close"
		self.time = 0
	def check(self):
		#sprawdza stan bramki, uplyw czasu, zmniejsza licznik czasu jesli czas nie minal
		if(self.state == "open"):
			if(self.time == 0):
				print "uplynal czas otwarcia"
				print " "
				self.state = "close"
				time.sleep(0.5)	
			else:
				print "czas do zamkniecia: " + str(self.time)
				self.time = self.time - 1
				time.sleep(0.5)
	def isClose(self):
		if(self.state == "close"):
			return True
		else:
			return False
