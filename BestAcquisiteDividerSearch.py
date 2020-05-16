# The best Acquisite Divider define, the round up cycle number is nearly equal with the 
# round down cycle number, which means each bits' error would be small, and the accumulate
# error of two bits would be small.
# Of course the best divider diff between 3~15
from BitCompensateSearch import BitCompensateSearch
import math
def BestAcquisiteDividerSearch(TargetFrequency,SysFrequency):
	GoodResult = []
	for AcqDivider in range(3,16):
		# print("\t\t\t\tThe Acquisite Divider : ",AcqDivider)
		Result = BitCompensateSearch(TargetFrequency,AcqDivider,SysFrequency)
		UpBitCompMethod 	= Result["RoundUpSolution"]
		DownBitCompMethod	= Result["RoundDownSolution"]
		UpTemp 		= UpBitCompMethod["CompUpNumber"] - UpBitCompMethod["CompDownNumber"]
		DownTemp 	= DownBitCompMethod["CompUpNumber"] - DownBitCompMethod["CompDownNumber"]
		if (math.fabs(UpTemp) <= 2) & (math.fabs(DownTemp) <= 2): #if the solution the difference between period number of round up and round down
			print("\t\tFound a Good choice")
			print(
				"\t\t\tUpBitCompMethod UpNumber:"	,	UpBitCompMethod["CompUpNumber"],
				"\tUpBitCompMethod DownNumber:"		,	UpBitCompMethod["CompDownNumber"],
				"\tUpFrequency:"					,	UpBitCompMethod["CompTargetFrequency"],
				"\tUpPeriodErr:"					,	UpBitCompMethod["CompTargetPeriodError"],
				'\n',
				"\t\t\tDownBitCompMethod UpNumber:"	,	DownBitCompMethod["CompUpNumber"],
				"\tDownBitCompMethod DownNumber:"	,	DownBitCompMethod["CompDownNumber"],
				"\tDownFrequency:"					,	DownBitCompMethod["CompTargetFrequency"],
				"\tDownPeriodErr:"					,	DownBitCompMethod["CompTargetPeriodError"],
				)
			GoodResult.append(Result)
		else:
			print("\t\t\t ")
	if len(GoodResult) == 0:
		print("\t\t\tOps! No Divider Founded")	
	return GoodResult
	
