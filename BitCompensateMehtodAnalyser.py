# This module would give out the compensate method performance analyse
from DividerAnalyser import DividerAnalyser
def BitCompensateMethodAnalyser(TargetFrequency, AcqDivider, SysFrequency, CompensateMethod):
	DividerInfo = DividerAnalyser(TargetFrequency, AcqDivider, SysFrequency)
	AcqNumber = AcqDivider + 1
	UpNumber = CompensateMethod / 16
	DownNumber = CompensateMethod % 16
	UpNumber = AcqNumber - DownNumber
# DividerAnalyser output -- Input information analyse
	TargetFrequency 						= DividerInfo["TargetFrequency"]
	TargetPeriod							= DividerInfo["TargetPeriod"]
	AcquisitionDivider						= DividerInfo["AcquisitionDivider"]
	AcquisitionFrequency					= DividerInfo["AcquisitionFrequency"]
	AcquisitionPeriod						= DividerInfo["AcquisitionPeriod"]
	SystemClockFrequency					= DividerInfo["SystemClockFrequency"]
	SystemClockPeriod						= DividerInfo["SystemClockPeriod"]
# DividerAnalyser output -- Round up analyse
	UpDivider								= DividerInfo["UpDivider"]
	UpTargetFrequency						= DividerInfo["UpTargetFrequency"]
	UpTargetPeriod							= DividerInfo["UpTargetPeriod"]
	UpAcquisitionFrequency					= DividerInfo["UpAcquisitionFrequency"]
	UpAcquisitionPeriod						= DividerInfo["UpAcquisitionPeriod"]
	UpTargetFrequencyError					= DividerInfo["UpTargetFrequencyError"]
	UpTargetPeriodError						= DividerInfo["UpTargetPeriodError"]
	UpAcquisitionFrequencyError				= DividerInfo["UpAcquisitionFrequencyError"]
	UpAcquisitionPeriodError				= DividerInfo["UpAcquisitionPeriodError"]
	UpTargetFrequencyRelativeError			= DividerInfo["UpTargetFrequencyRelativeError"]
	UpTargetPeriodRelativeError				= DividerInfo["UpTargetPeriodRelativeError"]
	UpAcquisitionFrequencyRelativeError		= DividerInfo["UpAcquisitionFrequencyRelativeError"]
	UpAcquisitionPeriodRelativeError		= DividerInfo["UpAcquisitionPeriodRelativeError"]
# DividerAnalyser output -- Round down analyse
	DownDivider								= DividerInfo["DownDivider"]
	DownTargetFrequency						= DividerInfo["DownTargetFrequency"]
	DownTargetPeriod						= DividerInfo["DownTargetPeriod"]
	DownAcquisitionFrequency				= DividerInfo["DownAcquisitionFrequency"]
	DownAcquisitionPeriod					= DividerInfo["DownAcquisitionPeriod"]
	DownTargetFrequencyError				= DividerInfo["DownTargetFrequencyError"]
	DownTargetPeriodError					= DividerInfo["DownTargetPeriodError"]
	DownAcquisitionFrequencyError			= DividerInfo["DownAcquisitionFrequencyError"]
	DownAcquisitionPeriodError				= DividerInfo["DownAcquisitionPeriodError"]
	DownTargetFrequencyRelativeError		= DividerInfo["DownTargetFrequencyRelativeError"]
	DownTargetPeriodRelativeError			= DividerInfo["DownTargetPeriodRelativeError"]
	DownAcquisitionFrequencyRelativeError	= DividerInfo["DownAcquisitionFrequencyRelativeError"]
	DownAcquisitionPeriodRelativeError		= DividerInfo["DownAcquisitionPeriodRelativeError"]
# Compensated output frequency information
	CompTargetFrequency 		= (UpNumber * UpTargetFrequency + DownNumber * DownTargetFrequency) / AcqNumber
	CompTargetPeriod 			= (UpNumber * UpTargetPeriod + DownNumber * DownTargetPeriod) / AcqNumber
	CompAcquisiteFrequency 		= (UpNumber * UpAcquisitionFrequency + DownNumber * DownAcquisitionFrequency) / AcqNumber
	CompAcquisitePeriod 		= (UpNumber * UpAcquisitionPeriod + DownNumber * DownAcquisitionPeriod) / AcqNumber
# Compensated output frequency error analyse 
	CompTargetFrequencyError	= CompTargetFrequency - TargetFrequency
	CompTargetPeriodError 		= CompTargetPeriod - TargetPeriod
	CompAcquisiteFrequencyError	= CompAcquisiteFrequency - AcquisitionFrequency
	CompAcquisitePeriodError	= CompAcquisitePeriod - AcquisitionPeriod
# 
	
	return LeftErrCompMethod
	pass