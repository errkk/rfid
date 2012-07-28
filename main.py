#!/usr/bin/python

import serial



class Rfid:
	dev_path = '/dev/ttyUSB0'

	def __init__(self):

		self.ser = serial.Serial( self.dev_path , 2400 )

	def listen(self):
		last = None
		while True:
			v = self.ser.readline()
			if v != last:
				last = v
				self.onread(v.rstrip())

	def onread(self,data):
		print data





def custom_onread(data):
	hashs = {
		'010A38FAAD' : 'Edog',
		'4D004A56E2' : 'Shiggins'
	}
	try:
		name = hashs[data]
	except KeyError:
		name = None

	print name



def main():
	rfid = Rfid()
	rfid.onread = custom_onread
	rfid.listen()

if __name__ == '__main__':
	main();

