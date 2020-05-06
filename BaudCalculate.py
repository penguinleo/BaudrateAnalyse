# from decimal import *
# calculate the actual baudrate with the system clock
# the error, the divider value.
import math 
def BaudCalculate(baud,clk):
	# getcontext().prec = 1
	baud_info = {	
					"clk":clk,
					"baudrate":baud,
					"DIV":0,
					"actual baudrate":0,
					"baudrate error":0,
					"relative error":0
					}
	Cal_Div = clk * math.pow(10,6) / baud
	# Div = Decimal(clk * 10^6) / Decimal(baud)
	Int_Div = round(Cal_Div)
	Act_Baud = clk * math.pow(10,6) / Int_Div
	Baud_Err = Act_Baud - baud
	Relat_Err = Baud_Err / Act_Baud
	baud_info = {	
					"clk":clk,
					"baudrate":baud,
					"DIV":Int_Div,
					"actual baudrate":Act_Baud,
					"baudrate error":Baud_Err,
					"relative error":Relat_Err
					}
	return baud_info