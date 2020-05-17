from BitCompensateSearch import BitCompensateSearch
from BestAcquisiteDividerSearch import BestAcquisiteDividerSearch
ResultList = BitCompensateSearch(115200,9,40)
BestChoice = BestAcquisiteDividerSearch(115200,39.9975)
# if len(BestChoice)==0:
#     print("\t\t\tNot found good Divider!")
# else:
#     print("\t\t\tFound good Choice")
#     for index in range(0,len(BestChoice)):
#         Choice = BestChoice[index]
#         UpBitCompMethod     = Choice["RoundUpSolution"]
#         DownBitCompMethod   = Choice["RoundDownSolution"]
#         print("\nBest Choice index:",index)
#         print("\tCompMethod",               UpBitCompMethod["CompMethod"],
#             "\tCompUpNumber",               UpBitCompMethod["CompUpNumber"],
#             "\tCompDownNumber",             UpBitCompMethod["CompDownNumber"],
#             "\tCompTargetFrequency",        UpBitCompMethod["CompTargetFrequency"],
#             "\tCompTargetPeriodError",      UpBitCompMethod["CompTargetPeriodError"],
#             )
#         print("\tCompMethod",               DownBitCompMethod["CompMethod"],
#             "\tCompUpNumber",               DownBitCompMethod["CompUpNumber"],
#             "\tCompDownNumber",             DownBitCompMethod["CompDownNumber"],
#             "\tCompTargetFrequency",        DownBitCompMethod["CompTargetFrequency"],
#             "\tCompTargetPeriodError",      DownBitCompMethod["CompTargetPeriodError"],
#             )
    # pass