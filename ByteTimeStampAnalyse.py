from BitTimeStampCalculate import BitTimeStampCalculate
def ByteTimeStampAnalyse(baud,div,clk,data):
	bits_number = 1 + 8 + 1 + 1
	start_time = 0
	bits_list = []
	for index in range(0,bits_number):
		bit_time_stamp = BitTimeStampCalculate(start_time,baud,div,clk)
		clock_time = bit_time_stamp["Clock Time"]
		bit_end_time = bit_time_stamp["Actual Stop Time"]
		start_time = bit_end_time + clock_time
		bits_list.append(bit_time_stamp)
	return bits_list