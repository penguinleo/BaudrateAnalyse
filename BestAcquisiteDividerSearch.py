# The best Acquisite Divider define, the round up cycle number is nearly equal with the 
# round down cycle number, which means each bits' error would be small, and the accumulate
# error of two bits would be small.
# Of course the best divider diff between 3~15
from BitCompensateSearch import BitCompensateSearch
import math
def BestAcquisiteDividerSearch(TargetFrequency,SysFrequency):
	ResultList = []
	for AcqDivider in range(3,16):
		# print("\t\t\t\tThe Acquisite Divider : ",AcqDivider)
		Result = BitCompensateSearch(TargetFrequency,AcqDivider,SysFrequency)
		UpBitCompMethod 	= Result["RoundUpSolution"]
		DownBitCompMethod	= Result["RoundDownSolution"]
		UpTemp 		= UpBitCompMethod["CompUpNumber"] - UpBitCompMethod["CompDownNumber"]
		DownTemp 	= DownBitCompMethod["CompUpNumber"] - DownBitCompMethod["CompDownNumber"]
		if (math.fabs(temp) <= 2) & (math.fabs(temp) <= 2): #if the solution the difference between period number of round up and round down
			print("\t\tFound a Good choice")
			print(
				"\t\t\tUpNumber:"	,	RoundUpList[index]["CompUpNumber"],
				"\tDownNumber:"		,	RoundUpList[index]["CompDownNumber"],
				"\tFrequency:"		,	RoundUpList[index]["CompTargetFrequency"],
				"\tPeriodErr:"		,	RoundUpList[index]["CompTargetPeriodError"]
				# '\n'
				)
		if len(ResultList_Up)!=0 & len(ResultList_Down)!=0 :
			print("\t\tThis divider is a best choice AcqDivider:", AcqDivider)
			ResultChoice = {
				"DividerInformation"			: Result["SolutionList"]
				"BestRoundUpDividerSolution" 	: ResultList_Up[0],
				"BestRoundDownDividerSolution"	: ResultList_Down[0]
			}	
			ResultList.append(ResultChoice)
			print(
				"\t\tThe Best Divider Found!\n",

				)
	return ResultList
	
