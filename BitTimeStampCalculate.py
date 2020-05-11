# calculate the start time and stop time of the bit
# the start time should be ns
# the start point is the first clk of the bit
from DividerAnalyser import DividerAnalyser
def BitTimeStampCalculate(start,baud,div,clk):
	baud_info 			= DividerAnalyser(baud,div,clk)
	BitStartTime 		= start
	BitStopTime 		= BitStartTime + baud_info["TargetPeriod"]
	UpBitStopTime 		= BitStartTime + baud_info["UpTargetPeriod"]
	UpBitPeriodError 	= baud_info["UpTargetPeriodError"]
	DownBitStopTime 	= BitStartTime + baud_info["DownTargetPeriod"]
	DownBitPeriodError 	= baud_info["DownTargetPeriodError"]
	BitTimeDic = {
		"BitStartTime" 		:	BitStartTime,
		"BitStopTime"		: 	BitStopTime,
		"UpBitStopTime"		: 	UpBitStopTime,
		"UpBitPeriodError" 	: 	UpBitPeriodError,
		"DownBitStopTime"	: 	DownBitStopTime,
		"DownBitPeriodError": 	DownBitPeriodError,	
		"Serial_Data"		: 	1	
	}
	return BitTimeDic