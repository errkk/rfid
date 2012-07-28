#!/usr/bin/python
import serial

# connect port
ser = serial.Serial('/dev/ttyUSB0', 2400)


class Rfid:
	dev_path = '/dev/ttyUSB0'

	def __init__(self):

		self.serial.Serial( self.dev_path , 2400 )

	def itterator(self):
		while 1:
			yield self.serial.readline()


	def main(self):
		for i in self.itterator():
			print i 



def main():
	rfid = Rfid()
	rfid.main()

if __name__ == '__main__':
	main();