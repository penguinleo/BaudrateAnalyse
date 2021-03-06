from BitTimeStampCalculate import BitTimeStampCalculate
from DividerAnalyser import DividerAnalyser
# from BaudrateDivider import BaudrateDivider
def ByteTimeStampAnalyse(baud,div,clk,data):
	bits_number 	= 1 + 8 + 1 + 1
	start_time 		= 0
	up_start_time 	= 0
	down_start_time = 0
	bits_list 		= []
	up_bits_list 	= []
	down_bits_list 	= []
	parity_bit 		= ((data>>7)&1)^((data>>6)&1)^((data>>5)&1)^((data>>4)&1)^((data>>3)&1)^((data>>2)&1)^((data>>1)&1)^((data)&1)
	baud_info 		= DividerAnalyser(baud,div,clk)
	SystemClockPeriod = baud_info["SystemClockPeriod"]
	bit_time_stamp  = {}
	for index in range(0,bits_number):
		bit_time_stamp 		= BitTimeStampCalculate(start_time,baud,div,clk)
		bit_end_time 		= bit_time_stamp["BitStopTime"]
		start_time 			= bit_end_time + SystemClockPeriod
		up_bit_time_stamp 	= BitTimeStampCalculate(up_start_time,baud,div,clk)
		up_bit_end_time 	= up_bit_time_stamp["UpBitStopTime"]
		up_start_time 		= up_bit_end_time + SystemClockPeriod
		down_bit_time_stamp = BitTimeStampCalculate(down_start_time,baud,div,clk)
		down_bit_end_time 	= down_bit_time_stamp["DownBitStopTime"]
		down_start_time 	= down_bit_end_time + SystemClockPeriod
		if 	 index == 0:
			serial_out 		= 0
		elif index <= 8:
			serial_out 		= (data>>(8-index))&1
		elif index == 9:
			serial_out 		= parity_bit
		elif index == 10:
			serial_out 		= 1
		bit_time_stamp["Serial_Data"] = serial_out
		up_bit_time_stamp["Serial_Data"] = serial_out
		down_bit_time_stamp["Serial_Data"] = serial_out
		bits_list.append(bit_time_stamp)
		up_bits_list.append(up_bit_time_stamp)
		down_bits_list.append(down_bit_time_stamp)
	byte_timestamp_list = {
		"baudrate_info"	: 	baud_info,
		"bits_list"		:	bits_list,
		"up_bits_list"	:	up_bits_list,
		"down_bits_list":	down_bits_list
	}
	return byte_timestamp_list