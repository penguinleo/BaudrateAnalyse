# this module help to calculate the error of the baudrate 
from BaudCalculate import BaudCalculate
import math
def BaudrateDivider(baud,div,clk):
	Second_ns = 1 * math.pow(10,9)
	Second_us = 1 * math.pow(10,6)
	acq_rate = baud * (div + 1)
	baud_info_temp = BaudCalculate(acq_rate,clk)
	act_baud = baud_info_temp["actual_baudrate"] * (div + 1)
	err_baud = act_baud - baud
	rela_err_baud = err_baud / act_baud
	bit_time_cal = Second_ns / baud
	bit_time_act = baud_info_temp["actual_bit_time"] * (div + 1)
	bit_time_err = bit_time_act - bit_time_cal
	bit_time_rel_err = bit_time_err / bit_time_act
	acq_time_rel_err = baud_info_temp["bit_time_error"] / baud_info_temp["actual_bit_time"]
	baud_info = {	
					"clk":baud_info_temp["clk"],
					"baudrate":baud,
					"DIV":baud_info_temp["DIV"],
					"BDIV":div,
					"actual_baudrate":act_baud,
					"baudrate_error":err_baud,
					"relative_baud_error":rela_err_baud,
					"bit_time":bit_time_cal,
					"clock_time":baud_info_temp["clock_time"],
					"actual_bit_time":bit_time_act,
					"bit_time_error":bit_time_err,
					"relative_error_maximum":bit_time_rel_err,
					"acquisite_rate_calculate":acq_rate,
					"acquisite_rate_actual":baud_info_temp["actual_baudrate"],
					"acquisite_rate_err":baud_info_temp["baudrate_error"],
					"acquisite_rate_err_relative":baud_info_temp["relative_baud_error"],
					"acquisite_period_calculated":baud_info_temp["bit_time"],
					"acquisite_period_actual":baud_info_temp["actual_bit_time"],
					"acquisite_period_err":baud_info_temp["bit_time_error"],
					"acquisite_period_err_relative":acq_time_rel_err
					}
	return baud_info
	pass