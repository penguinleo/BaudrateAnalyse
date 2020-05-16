from BitCompensateSearch import BitCompensateSearch
from BestAcquisiteDividerSearch import BestAcquisiteDividerSearch
ResultList = BitCompensateSearch(115200,9,40)
BestChoice = BestAcquisiteDividerSearch(115200,40)
if len(BestChoice)==0:
	print("\t\t\tNot found good Divider!")
else:
	print("\t\t\tFound good Choice")
	for index in range(0,len(BestChoice)):
		Choice = BestChoice[index]
		UpBitCompMethod 	= Choice["RoundUpSolution"]
		DownBitCompMethod 	= Choice["RoundDownSolution"]
		print("Best Choice index:",index)
		print("\t",UpBitCompMethod)
		print("\t",DownBitCompMethod)
	pass