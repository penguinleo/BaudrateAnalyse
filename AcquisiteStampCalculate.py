# this module calculates the acquisition period start time and stop time
# give out the round up stamp and round down stamp with their error.
from DividerAnalyser import DividerAnalyser
def AcquisiteStampCalculate(start,baud,div,clk):
	baud_info 					= DividerAnalyser(baud,div,clk)
	AcquisiteStartStamp			= start
	AcquisiteStopStamp 			= AcquisiteStartStamp + baud_info["AcquisitionPeriod"]
	UpAcquisiteStopStamp 		= AcquisiteStartStamp + baud_info["UpAcquisitionPeriod"]
	UpAcquisitePeriodError 		= baud_info["UpAcquisitionPeriodError"]
	DownAcquisiteStopStamp 		= AcquisiteStartStamp + baud_info["DownAcquisitionPeriod"]
	DownAcquisitePeriodError 	= baud_info["DownAcquisitionPeriodError"]
	AcquisiteStampDic = {
		"AcquisiteStartStamp" 		: 	AcquisiteStartStamp,
		"AcquisiteStopStamp"		: 	AcquisiteStopStamp,
		"UpAcquisiteStopStamp"		: 	UpAcquisiteStopStamp,
		"UpAcquisitePeriodError" 	:	UpAcquisitePeriodError,
		"DownAcquisiteStopStamp"	:	DownAcquisiteStopStamp,
		"DownAcquisitePeriodError"	:	DownAcquisitePeriodError,
	}
	return AcquisiteStampDic