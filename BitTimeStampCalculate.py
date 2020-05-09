# calculate the start time and stop time of the bit
# the start time should be ns
# the start point is the first clk of the bit
from BaudrateDivider import BaudrateDivider
def BitTimeStampCalculate(start,baud,div,clk):
	baud_info = BaudrateDivider(baud,div,clk)
	start_time = start
	real_stop_time = baud_info["actual_bit_time"] + start
	requair_stop_time = baud_info["bit_time"] + start
	bit_period_err = baud_info["bit_time_error"]
	clock_period = baud_info["clock_time"]
	bit_time_stamp = {
		"Start Time": start_time,
		"Actual Stop Time": real_stop_time,
		"Calculated Stop Time": requair_stop_time,
		"Bit Time Error": bit_period_err,
		"Clock Time": clock_period
	}
	return bit_time_stamp
	pass