
import sys
from random import randint
import time
from cnt import Cnt
from g import G
from man import man





if __name__ == '__main__':
	czlowiek = man()
	bramka = Cnt()
	stan = G()
	while (1):

		if(stan.isClose()):
			#jesli tak to przyjmij monete
			bramka.getCoin(czlowiek.putCoin())
			#spawdz czy nie zepsul
			bramka.isBroken()
			if(bramka.isFull()):
				stan.openit();
		else:
			stan.check()
