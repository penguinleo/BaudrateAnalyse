# from decimal import *
# calculate the actual baudrate with the system clock
# the error, the divider value.
# this module give out the minimum error of the baudrate
# with the system clock
import math 
def BaudCalculate(baud,clk):
	# getcontext().prec = 1
	baud_info = {	
					"clk":clk,
					"baudrate":baud,
					"DIV":0,
					"actual_baudrate":0,
					"baudrate_error":0,
					"relative_error":0
					}
	Second_ns = 1 * math.pow(10,9)
	Second_us = 1 * math.pow(10,6)
	Cal_Div = clk * Second_us / baud
	# Div = Decimal(clk * 10^6) / Decimal(baud)
	Int_Div = round(Cal_Div)
	Act_Baud = clk * Second_us / Int_Div
	Baud_Err = Act_Baud - baud
	Relat_Err = Baud_Err / Act_Baud 
	Bit_Time = Second_ns / baud
	Clock_Time = Second_ns / Second_us / clk
	Act_BitTime = Clock_Time * Int_Div
	BitTime_Err = Act_BitTime - Bit_Time
	Relat_BitTime_Err = BitTime_Err / Act_BitTime
	Relat_Err_Max = 1 / (2 * Int_Div - 1) 
	baud_info = {	
					"clk":clk,
					"baudrate":baud,
					"DIV":Int_Div,
					"actual_baudrate":Act_Baud,
					"baudrate_error":Baud_Err,
					"relative_baud_error":Relat_Err,
					"bit_time":Bit_Time,
					"clock_time":Clock_Time,
					"actual_bit_time":Act_BitTime,
					"bit_time_error":BitTime_Err,
					"relative_error_maximum":Relat_Err_Max
					}
	return baud_info