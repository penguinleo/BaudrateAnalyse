# this module help to search best compensate method
from BitCompensateMethodAnalyser import BitCompensateMethodAnalyser
from DividerAnalyser import DividerAnalyser
import math
def BitCompensateSearch(TargetFrequency, AcqDivider, SysFrequency):
	ErrorLimit = DividerAnalyser(TargetFrequency, 0, SysFrequency)
	AcqNumber = AcqDivider + 1
	BitCompensateTarget = {
		"BitCompUpDivider" 									: ErrorLimit["UpDivider"],
		"BitCompUpTargetFrequency" 							: ErrorLimit["UpTargetFrequency"],
		"BitCompUpTargetPeriod" 							: ErrorLimit["UpTargetPeriod"],
		"BitCompUpAcquisitionFrequency" 					: ErrorLimit["UpAcquisitionFrequency"],
		"BitCompUpAcquisitionPeriod" 						: ErrorLimit["UpAcquisitionPeriod"],
		"BitCompUpTargetFrequencyError" 					: ErrorLimit["UpTargetFrequencyError"],
		"BitCompUpTargetPeriodError" 						: ErrorLimit["UpTargetPeriodError"],
		"BitCompUpAcquisitionFrequencyError" 				: ErrorLimit["UpAcquisitionFrequencyError"],
		"BitCompUpAcquisitionPeriodError" 					: ErrorLimit["UpAcquisitionPeriodError"],
		"BitCompUpTargetFrequencyRelativeError" 			: ErrorLimit["UpTargetFrequencyRelativeError"],
		"BitCompUpTargetPeriodRelativeError" 				: ErrorLimit["UpTargetPeriodRelativeError"],
		"BitCompUpAcquisitionFrequencyRelativeError" 		: ErrorLimit["UpAcquisitionFrequencyRelativeError"],
		"BitCompUpAcquisitionPeriodRelativeError" 			: ErrorLimit["UpAcquisitionPeriodRelativeError"],		
		"BitCompDownDivider" 								: ErrorLimit["DownDivider"],
		"BitCompDownTargetFrequency" 						: ErrorLimit["DownTargetFrequency"],
		"BitCompDownTargetPeriod" 							: ErrorLimit["DownTargetPeriod"],
		"BitCompDownAcquisitionFrequency" 					: ErrorLimit["DownAcquisitionFrequency"],
		"BitCompDownAcquisitionPeriod" 						: ErrorLimit["DownAcquisitionPeriod"],
		"BitCompDownTargetFrequencyError" 					: ErrorLimit["DownTargetFrequencyError"],
		"BitCompDownTargetPeriodError" 						: ErrorLimit["DownTargetPeriodError"],
		"BitCompDownAcquisitionFrequencyError" 				: ErrorLimit["DownAcquisitionFrequencyError"],
		"BitCompDownAcquisitionPeriodError" 				: ErrorLimit["DownAcquisitionPeriodError"],
		"BitCompDownTargetFrequencyRelativeError" 			: ErrorLimit["DownTargetFrequencyRelativeError"],
		"BitCompDownTargetPeriodRelativeError" 				: ErrorLimit["DownTargetPeriodRelativeError"],
		"BitCompDownAcquisitionFrequencyRelativeError" 		: ErrorLimit["DownAcquisitionFrequencyRelativeError"],
		"BitCompDownAcquisitionPeriodRelativeError" 		: ErrorLimit["DownAcquisitionPeriodRelativeError"]		
		}
	# print(
	# 	'\n',
	# 	"BitCompUpTargetFrequencyError" 	,":", BitCompensateTarget["BitCompUpTargetFrequencyError"], 	'\n',
	# 	"BitCompUpTargetPeriodError"		,":", BitCompensateTarget["BitCompUpTargetPeriodError"],		'\n',
	# 	"BitCompDownTargetFrequencyError"	,":", BitCompensateTarget["BitCompDownTargetFrequencyError"],		'\n',
	# 	"BitCompDownTargetPeriodError"		,":", BitCompensateTarget["BitCompDownTargetPeriodError"],			'\n'
	# 	)
	print("\n\n\t\tSearching for AcqDivider:",AcqDivider)
	ResultList = []
	UpCompList = []
	DownCompList = []
	ErrorPlotList = []
	for DownNumber in range(0,AcqNumber+1):
		Result = BitCompensateMethodAnalyser(TargetFrequency, AcqDivider, SysFrequency,DownNumber)
		print(
			"UpNumber:"		,	Result["CompUpNumber"],
			"\tDownNumber:"	,	Result["CompDownNumber"],
			"\tFrequency:"	,	Result["CompTargetFrequency"],
			"\tPeriodErr:"	,	Result["CompTargetPeriodError"]
			# '\n'
			)
		Up_Diff = Result["CompTargetPeriodError"] - BitCompensateTarget["BitCompUpTargetPeriodError"]
		Down_Diff = Result["CompTargetPeriodError"] - BitCompensateTarget["BitCompDownTargetPeriodError"]
		if math.fabs(Up_Diff) < 0.0005:
			UpCompList.append(Result)
		if math.fabs(Down_Diff) < 0.0005:
			DownCompList.append(Result)
		ResultList.append(Result)
	# print(ResultList)
	print("\t\t\tThe Search result")
	print("\tDivider Round Up: ", Result["UpDivider"],"\t Divider Round Down: ",Result["DownDivider"])
	print("\tThe Round Up Solution")
	for index in range(0,len(UpCompList)):
		print(
			"\t\t\tUpNumber:"		,	UpCompList[index]["CompUpNumber"],
			"\tDownNumber:"	,	UpCompList[index]["CompDownNumber"],
			"\tFrequency:"	,	UpCompList[index]["CompTargetFrequency"],
			"\tPeriodErr:"	,	UpCompList[index]["CompTargetPeriodError"]
			# '\n'
			)
		pass
	print("\tThe Round Down Solution")
	for index in range(0,len(DownCompList)):
		print(
			"\t\t\tUpNumber:"		,	DownCompList[index]["CompUpNumber"],
			"\tDownNumber:"	,	DownCompList[index]["CompDownNumber"],
			"\tFrequency:"	,	DownCompList[index]["CompTargetFrequency"],
			"\tPeriodErr:"	,	DownCompList[index]["CompTargetPeriodError"]
			# '\n'
			)
		pass
	if len(UpCompList) !=0:
		UpBitCompMethod = UpCompList[0]
	else:
		UpBitCompMethod = {}
	if len(DownCompList) !=0:
		DownBitCompMethod = DownCompList[0]
	else:
		DownBitCompMethod = {}
	Result = {
		"SolutionList" 		: ResultList,
		"RoundUpSolution" 	: UpBitCompMethod,
		"RoundDownSolution"	: DownBitCompMethod
	}
	return Result
	pass