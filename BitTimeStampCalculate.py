# calculate the start time and stop time of the bit
# the start time should be ns
# the start point is the first clk of the bit
from DividerAnalyser import DividerAnalyser
from AcquisiteStampCalculate import AcquisiteStampCalculate
def BitTimeStampCalculate(start,baud,div,clk):
	baud_info 					= DividerAnalyser(baud,div,clk)
	BitStartTime 				= start
	BitStopTime 				= BitStartTime + baud_info["TargetPeriod"]
	UpBitStopTime 				= BitStartTime + baud_info["UpTargetPeriod"]
	UpBitPeriodError 			= baud_info["UpTargetPeriodError"]
	DownBitStopTime 			= BitStartTime + baud_info["DownTargetPeriod"]
	DownBitPeriodError 			= baud_info["DownTargetPeriodError"]
	SystemClockPeriod 			= baud_info["SystemClockPeriod"]
	AcquisiteStampList 			= []
	AcquisiteStartTime  		= 0 
	UpAcquisiteStartTime 		= 0
	DownAcquisiteStartTime 		= 0
	UpAcquisiteStampList 		= []
	DownAcquisiteStampList 		= []
	for AcqIndex in range(0,(div+1)):
		AcquisiteStampDic 		= AcquisiteStampCalculate(AcquisiteStartTime,baud,div,clk)
		AcquisiteStopTime 		= AcquisiteStampDic["AcquisiteStopStamp"]
		AcquisiteStartTime 		= AcquisiteStopTime + SystemClockPeriod
		UpAcquisiteStampDic 	= AcquisiteStampCalculate(UpAcquisiteStartTime,baud,div,clk)
		UpAcquisiteStopTime 	= UpAcquisiteStampDic["UpAcquisiteStopStamp"]
		UpAcquisiteStartTime	= UpAcquisiteStopTime + SystemClockPeriod
		DownAcquisiteStampDic 	= AcquisiteStampCalculate(DownAcquisiteStartTime,baud,div,clk)
		DownAcquisiteStopTime 	= DownAcquisiteStampDic["DownAcquisiteStopStamp"]
		DownAcquisiteStartTime	= DownAcquisiteStopTime + SystemClockPeriod
		AcquisiteStampDic 		= {
			"AcquisiteStartStamp" 		: 	AcquisiteStampDic["AcquisiteStartStamp"] + BitStartTime,
			"AcquisiteStopStamp"		: 	AcquisiteStampDic["AcquisiteStopStamp"] + BitStartTime,
			"UpAcquisiteStopStamp"		: 	AcquisiteStampDic["UpAcquisiteStopStamp"] + BitStartTime,
			"UpAcquisitePeriodError" 	:	AcquisiteStampDic["UpAcquisitePeriodError"],
			"DownAcquisiteStopStamp"	:	AcquisiteStampDic["DownAcquisiteStopStamp"] + BitStartTime,
			"DownAcquisitePeriodError"	:	AcquisiteStampDic["DownAcquisitePeriodError"],
		}
		UpAcquisiteStampDic 	= {
			"AcquisiteStartStamp" 		: 	UpAcquisiteStampDic["AcquisiteStartStamp"] + BitStartTime,
			"AcquisiteStopStamp"		: 	UpAcquisiteStampDic["AcquisiteStopStamp"] + BitStartTime,
			"UpAcquisiteStopStamp"		: 	UpAcquisiteStampDic["UpAcquisiteStopStamp"] + BitStartTime,
			"UpAcquisitePeriodError" 	:	UpAcquisiteStampDic["UpAcquisitePeriodError"],
			"DownAcquisiteStopStamp"	:	UpAcquisiteStampDic["DownAcquisiteStopStamp"] + BitStartTime,
			"DownAcquisitePeriodError"	:	UpAcquisiteStampDic["DownAcquisitePeriodError"],
		}
		DownAcquisiteStampDic 	= {
			"AcquisiteStartStamp" 		: 	DownAcquisiteStampDic["AcquisiteStartStamp"] + BitStartTime,
			"AcquisiteStopStamp"		: 	DownAcquisiteStampDic["AcquisiteStopStamp"] + BitStartTime,
			"UpAcquisiteStopStamp"		: 	DownAcquisiteStampDic["UpAcquisiteStopStamp"] + BitStartTime,
			"UpAcquisitePeriodError" 	:	DownAcquisiteStampDic["UpAcquisitePeriodError"],
			"DownAcquisiteStopStamp"	:	DownAcquisiteStampDic["DownAcquisiteStopStamp"] + BitStartTime,
			"DownAcquisitePeriodError"	:	DownAcquisiteStampDic["DownAcquisitePeriodError"],
		}
		AcquisiteStampList.append(AcquisiteStampDic)
		DownAcquisiteStampList.append(DownAcquisiteStampDic)
		UpAcquisiteStampList.append(UpAcquisiteStampDic)
	
	BitTimeDic = {
		"BitStartTime" 				:	BitStartTime,
		"BitStopTime"				: 	BitStopTime,
		"AcquisiteStampList"		:	AcquisiteStampList,
		"UpBitStopTime"				: 	UpBitStopTime,
		"UpBitPeriodError" 			: 	UpBitPeriodError,
		"UpAcquisiteStampList"		:	UpAcquisiteStampList,
		"DownBitStopTime"			: 	DownBitStopTime,
		"DownBitPeriodError"		: 	DownBitPeriodError,	
		"DownAcquisiteStampList"	:	DownAcquisiteStampList,
		"Serial_Data"				: 	1	
	}
	return BitTimeDic