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
		RoundUpList 	= Result["RoundUpSolution"]
		RoundDownList	= Result["RoundDownSolution"]
		ResultList_Up = []
		ResultList_Down = []
		for index in range(0,len(RoundUpList)):
			temp = RoundUpList[index]["CompUpNumber"] - RoundUpList[index]["CompDownNumber"]
			if math.fabs(temp) <= 2: #if the solution the difference between period number of round up and round down
				print("\t\tFound a round-up choice")
				print(
					"\t\t\tUpNumber:"	,	RoundUpList[index]["CompUpNumber"],
					"\tDownNumber:"		,	RoundUpList[index]["CompDownNumber"],
					"\tFrequency:"		,	RoundUpList[index]["CompTargetFrequency"],
					"\tPeriodErr:"		,	RoundUpList[index]["CompTargetPeriodError"]
					# '\n'
					)
				ResultList_Up.append(RoundUpList[index])
		for index in range(0,len(RoundDownList)):
			temp = RoundDownList[index]["CompUpNumber"] - RoundDownList[index]["CompDownNumber"]
			if math.fabs(temp) <= 2: #if the solution the difference between period number of round up and round down
				print("\t\tFound a round-down choice")
				print(
					"\t\t\tUpNumber:"	,	RoundDownList[index]["CompUpNumber"],
					"\tDownNumber:"		,	RoundDownList[index]["CompDownNumber"],
					"\tFrequency:"		,	RoundDownList[index]["CompTargetFrequency"],
					"\tPeriodErr:"		,	RoundDownList[index]["CompTargetPeriodError"]
					# '\n'
					)
				ResultList_Down.append(RoundDownList[index])
		if len(ResultList_Up)!=0 & len(ResultList_Down)!=0 :
			print("\t\tThis divider is a best choice AcqDivider:", AcqDivider)
			ResultChoice = {
				"BestRoundUpDivider" 	: ResultList_Up[0],
				"BestRoundDownDivider"	: ResultList_Down[0]
			}	
			ResultList.append(ResultChoice)
			print()
	return ResultList
	
