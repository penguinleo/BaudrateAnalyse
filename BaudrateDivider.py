# this module help to calculate the error of the baudrate 
from BaudCalculate import BaudCalculate
import math
def BaudrateDivider(baud,div,clk):
	Second_ns = 1 * math.pow(10,9)
	Second_us = 1 * math.pow(10,6)
	acq_rate = baud * (div + 1)
	baud_info_temp = BaudCalculate(acq_rate,clk)
	baud_info = {	
					"clk":baud_info_temp["clk"],
					"baudrate":baud,
					"DIV":baud_info_temp["DIV"],
					"BDIV":div,
					"actual_baudrate":baud_info_temp["actual_baudrate"],
					"baudrate_error":baud_info_temp["baudrate_error"],
					"relative_baud_error":baud_info_temp["relative_baud_error"],
					"bit_time":baud_info_temp["bit_time"],
					"clock_time":baud_info_temp["clock_time"],
					"actual_bit_time":baud_info_temp["actual_bit_time"],
					"bit_time_error":baud_info_temp["bit_time_error"],
					"relative_error_maximum":baud_info_temp["relative_error_maximum"]
					}
	return baud_info
	pass