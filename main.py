#!/usr/bin/python

import serial, datetime



class Rfid:
	dev_path = '/dev/ttyUSB0'
	interval = datetime.timedelta(seconds=5)

	def __init__(self):
		"Setup serial connection to the reader"
		try:
			self.ser = serial.Serial( self.dev_path , 2400 )
		except serial.serialutil.SerialException:
			self.dev_path = '/dev/ttys000'
			self.ser = serial.Serial( self.dev_path , 2400 )
		else:
			print 'Connected on %s' % self.dev_path

	def listen(self):
		"Listen for new lines comingin, run a callback function when a new one comes in"
		last = None, datetime.datetime.now()

		# Loop infinitly
		while True:
			v = self.ser.readline()
			now = datetime.datetime.now()
			delta = now - last[1]
			# If the ID is different to last time, or the interval has elapsed then run the callback
			if v != last[0] or delta > self.interval:
				last = v, datetime.datetime.now()
				self.onread(v.rstrip())

	def onread(self,data):
		"Defualt read function, print out the data"
		print data





def custom_onread(data):
	hashs = {
		'010A38FAAD' : 'Edog',
		'4D004A56E2' : 'Shiggins'
	}
	try:
		name = hashs[data]
	except KeyError:
		name = data

	print name



def main():
	rfid = Rfid()
	rfid.onread = custom_onread
	rfid.listen()


if __name__ == '__main__':
	main();

