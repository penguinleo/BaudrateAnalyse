# this file is help to calculate the error of give clock frequency
# with all 600bps baudrate from 600 to 115200 even over 2006400 bps
from BaudCalculate import BaudCalculate
def BaudAnalyse(clk):
	index = 0
	baud = 600
	step = 600
	baud_info_list = []
	for index in range(0,3500):
		baudrate = baud + index * step
		baud_info_list.append(BaudCalculate(baudrate,clk))
		pass
	# print(baud_info_list)
	return baud_info_list
	pass 