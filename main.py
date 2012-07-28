#!/usr/bin/python
import serial




class Rfid:
	dev_path = '/dev/ttyUSB0'

	def __init__(self):

		self.ser = serial.Serial( self.dev_path , 2400 )

	def main(self):
		while True:
			print self.ser.readline() 

def main():
	rfid = Rfid()
	rfid.main()

if __name__ == '__main__':
	main();
