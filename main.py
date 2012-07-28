#!/usr/bin/python
import serial




class Rfid:
	dev_path = '/dev/ttyUSB0'

	def __init__(self):

		self.ser = serial.Serial( self.dev_path , 2400 )

	def itterator(self):
		while 1:
			yield self.ser.readline()


	def main(self):
		for i in self.itterator():
			print i 



def main():
	rfid = Rfid()
	rfid.main()

if __name__ == '__main__':
	main();