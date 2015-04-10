import sys
from random import randint
import time

class man():
	def putCoin(self):
		x = randint(0,10000)
		#szansa 1 na 1000, ze czowiek wepchnie cos innego niz moneta 
		if(x == 155):
			print "czlowiek psuje bramke"
			return -1
		else:
		#zwrocenie monety o nominale 1,2 lub 3
			x = randint(1,3)
			print "czlowiek wrzuca monete o nominale : " + str(x)
			time.sleep(0.5)
			return x;
