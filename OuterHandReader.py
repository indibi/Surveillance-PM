from smbus2 import SMBus
from mlx90614 import MLX90614
import time, random, os
import HCSR04

#	HandReader = OHandReader(12,18,1)
# def main():
# 	try:
# 		os.nice(-5)
# 	except OSError:
# 		print("Process priority could not be decreased!")
#
#
#
# if __name__ == '__main__':
# 	main()

STATE = None
HAND_APPROVED = 1
HAND_DENIED =0
NOT_HAND = 2

class OHandReader(object):
	LOCKED = -10
	UNLOCKED = 100
	VERIFICATION = 10
	DORMANT = 50
	STATE = DORMANT

	def __init__(self, trig_pin, echo_pin, i2c_bus = 1):
		self.bus = SMBus(i2c_bus)
		self.IRSens = MLX90614(self.bus)
		self.ProxSens= HCSR04.HCSR_04(trig_pin, echo_pin, self.IRSens.get_ambient())

	def read(self):
		self.ProxSens.set_temp(self.IRSens.get_ambient())
		Temperature_list = []
		while STATE = VERIFICATION:
			dist = self.ProxSens.distance()
			count =1
			## Count counts the number of measurement trials that was done to
			## get a healthy reading. Unhealthy ones are discarded.
			while((dist>=400) or (dist<2.5)):
				count = count+1
				time.sleep(0.01)
				dist = self.ProxSens.distance()
				if count == 60:
					break

			#print(f"Distance = {dist}")
			if (dist <= 6) or (count==60): 	# Hand is within range
				print("Object in range")
				if count!=60:
					print(f"Distance = {dist}")
				for x in range(5):			# Getting 5 temperature measurements
					self.Temperature_list.append(1.02* self.IRSens.get_object_1())
					time.sleep(0.100)
				
				max_temp = max(self.Temperature_list)
				print(f"Temperature reading: {max_temp}")
				self.Temperature_list.clear()
				if (37.5>max_temp>26):		# Hand temperature is eligible
					print("Hand approved!")
					return HAND_APPROVED
				elif(max_temp >=37.5):
					print("Hand denied!")
					return HAND_DENIED
				else:
					print("Unknown object is obscuring the Outer Hand Reader!")
					return NOT_HAND

			count =0
			time.sleep(0.2)