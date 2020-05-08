# this module help generate the standard serial data in the uart line
# the accurate of the wave is defined by the clk(Mhz)
import math
from BaudCalculate import BaudCalculate
def SerialSendWave(baudrate, clk, data):
	bits_number = 1 + 8 + 1 + 1
	Second_ns = 1 * math.pow(10,9)
	Second_us = 1 * math.pow(10,6)
	quatum_clk = Second_ns / Second_us / clk
# define the bit width, the accurate of the baudrate wave is defined by the clk
	bit_points_number = int(round(clk * Second_us / baudrate))
	byte_points_number = bit_points_number * bits_number
# parity calculate
	parity_bit = ((data>>7)&1)^((data>>6)&1)^((data>>5)&1)^((data>>4)&1)^((data>>3)&1)^((data>>2)&1)^((data>>1)&1)^((data)&1)
	print(parity_bit)
# wave data
	wave_list = []
	wave_data = {}
# wave generate
	for bits_index in range(0,bits_number):
		print(bits_index)
		if bits_index == 0:
			serial_out = 0
		elif bits_index <= 8:
			serial_out = (data>>(8-bits_index))&1
		elif bits_index == 9:
			serial_out = parity_bit
		elif bits_index == 10:
			serial_out = 1
	# the bit width delay and wave data store
		for bit_width_cnt in range(0,bit_points_number-1):
			wave_data = {
				"Value": serial_out,
				"Time": ((bits_index*bit_points_number)+bit_width_cnt)*quatum_clk
			}
			wave_list.append(wave_data)
	return wave_list