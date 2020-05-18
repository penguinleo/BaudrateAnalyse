from BitCompensateSearch import BitCompensateSearch
from BestAcquisiteDividerSearch import BestAcquisiteDividerSearch
ResultList = BitCompensateSearch(115200,9,40)
BestChoice = BestAcquisiteDividerSearch(115200,40)
print("\n\n\n")
if len(BestChoice)==0:
    print("\t\t\tNot found good Divider!")
else:
    print("\t\t\tFound good Choice")
    for index in range(0,len(BestChoice)):
        Choice = BestChoice[index]
        UpBitCompMethod     = Choice["RoundUpSolution"]
        DownBitCompMethod   = Choice["RoundDownSolution"]
        print("Best Choice index:",index)
        print("\tRound Up Compensate Method:")
        # print("\t\tCompMethod",               UpBitCompMethod["CompMethod"],
        #     "\tCompUpNumber",               UpBitCompMethod["CompUpNumber"],
        #     "\tCompDownNumber",             UpBitCompMethod["CompDownNumber"],
        #     "\tCompTargetFrequency",        UpBitCompMethod["CompTargetFrequency"],
        #     "\tCompTargetPeriodError",      UpBitCompMethod["CompTargetPeriodError"],
        #     )
        print(
			# The Require frequency infomation
				# "\t\tTargetFrequency" 						, UpBitCompMethod["TargetFrequency"],
				# "\tTargetPeriod" 							, UpBitCompMethod["TargetPeriod"],
				# "\tAcquisitionDivider" 						, UpBitCompMethod["AcquisitionDivider"],
				# "\tAcquisitionFrequency" 					, UpBitCompMethod["AcquisitionFrequency"],
				# "\tAcquisitionPeriod" 						, UpBitCompMethod["AcquisitionPeriod"],
				# "\tSystemClockFrequency" 					, UpBitCompMethod["SystemClockFrequency"],
				# "\tSystemClockPeriod" 						, UpBitCompMethod["SystemClockPeriod"], 
			# Round Up analyser output 
				# "\tUpDivider"								, UpBitCompMethod["UpDivider"],
				# "\tUpTargetFrequency"						, UpBitCompMethod["UpTargetFrequency"],
				# "\tUpTargetPeriod"							, UpBitCompMethod["UpTargetPeriod"],
				# "\tUpAcquisitionFrequency"					, UpBitCompMethod["UpAcquisitionFrequency"],
				# "\tUpAcquisitionPeriod"						, UpBitCompMethod["UpAcquisitionPeriod"],
				# "\tUpTargetFrequencyError"					, UpBitCompMethod["UpTargetFrequencyError"],
				# "\tUpTargetPeriodError"						, UpBitCompMethod["UpTargetPeriodError"],
				# "\tUpAcquisitionFrequencyError"				, UpBitCompMethod["UpAcquisitionFrequencyError"],
				# "\tUpAcquisitionPeriodError"				, UpBitCompMethod["UpAcquisitionPeriodError"],
				# "\tUpTargetFrequencyRelativeError"			, UpBitCompMethod["UpTargetFrequencyRelativeError"],
				# "\tUpTargetPeriodRelativeError"				, UpBitCompMethod["UpTargetPeriodRelativeError"],
				# "\tUpAcquisitionFrequencyRelativeError"		, UpBitCompMethod["UpAcquisitionFrequencyRelativeError"],
				# "\tUpAcquisitionPeriodRelativeError"		, UpBitCompMethod["UpAcquisitionPeriodRelativeError"],	
			# Round Down analyser output
				# "\tDownDivider"								, UpBitCompMethod["DownDivider"],
				# "\tDownTargetFrequency"						, UpBitCompMethod["DownTargetFrequency"],
				# "\tDownTargetPeriod"						, UpBitCompMethod["DownTargetPeriod"],
				# "\tDownAcquisitionFrequency"				, UpBitCompMethod["DownAcquisitionFrequency"],
				# "\tDownAcquisitionPeriod"					, UpBitCompMethod["DownAcquisitionPeriod"],
				# "\tDownTargetFrequencyError"				, UpBitCompMethod["DownTargetFrequencyError"],
				# "\tDownTargetPeriodError"					, UpBitCompMethod["DownTargetPeriodError"],
				# "\tDownAcquisitionFrequencyError"			, UpBitCompMethod["DownAcquisitionFrequencyError"],
				# "\tDownAcquisitionPeriodError"				, UpBitCompMethod["DownAcquisitionPeriodError"],
				# "\tDownTargetFrequencyRelativeError"		, UpBitCompMethod["DownTargetFrequencyRelativeError"],
				# "\tDownTargetPeriodRelativeError"			, UpBitCompMethod["DownTargetPeriodRelativeError"],
				# "\tDownAcquisitionFrequencyRelativeError"	, UpBitCompMethod["DownAcquisitionFrequencyRelativeError"],		
				# "\tDownAcquisitionPeriodRelativeError"		, UpBitCompMethod["DownAcquisitionPeriodRelativeError"],
			# Compensate Output
				"\tCompMethod" 								, UpBitCompMethod["CompMethod"],
				"\tCompUpNumber" 							, UpBitCompMethod["CompUpNumber"],
				"\tCompDownNumber"							, UpBitCompMethod["CompDownNumber"],
				"\tCompTargetFrequency" 					, UpBitCompMethod["CompTargetFrequency"],
				"\tCompTargetPeriod" 						, UpBitCompMethod["CompTargetPeriod"],
				# "\tCompAcquisiteFrequency" 					, UpBitCompMethod["CompAcquisiteFrequency"],
				# "\tCompAcquisitePeriod" 					, UpBitCompMethod["CompAcquisitePeriod"],
				"\tCompTargetFrequencyError" 				, UpBitCompMethod["CompTargetFrequencyError"],
				"\tCompTargetPeriodError" 					, UpBitCompMethod["CompTargetPeriodError"],
				# "\tCompAcquisiteFrequencyError" 			, UpBitCompMethod["CompAcquisiteFrequencyError"],
				# "\tCompAcquisitePeriodError" 				, UpBitCompMethod["CompAcquisitePeriodError"],
				"\tCompTargetFrequencyRelativeError" 		, UpBitCompMethod["CompTargetFrequencyRelativeError"],
				# "\tCompTargetPeriodRelativeError" 			, UpBitCompMethod["CompTargetPeriodRelativeError"],
				# "\tCompAcquisiteFrequencyRelativeError" 	, UpBitCompMethod["CompAcquisiteFrequencyRelativeError"],
				# "\tCompAcquisitePeriodRelativeError" 		, UpBitCompMethod["CompAcquisitePeriodRelativeError"],
				"\t"	
        	)
        print("\tRound Down Compensate Method:")
        # print("\t\tCompMethod",               DownBitCompMethod["CompMethod"],
        #     "\tCompUpNumber",               DownBitCompMethod["CompUpNumber"],
        #     "\tCompDownNumber",             DownBitCompMethod["CompDownNumber"],
        #     "\tCompTargetFrequency",        DownBitCompMethod["CompTargetFrequency"],
        #     "\tCompTargetPeriodError",      DownBitCompMethod["CompTargetPeriodError"],
        #     )
        print(
			# The Require frequency infomation
				# "\t\tTargetFrequency" 						, DownBitCompMethod["TargetFrequency"],
				# "\tTargetPeriod" 							, DownBitCompMethod["TargetPeriod"],
				# "\tAcquisitionDivider" 						, DownBitCompMethod["AcquisitionDivider"],
				# "\tAcquisitionFrequency" 					, DownBitCompMethod["AcquisitionFrequency"],
				# "\tAcquisitionPeriod" 						, DownBitCompMethod["AcquisitionPeriod"],
				# "\tSystemClockFrequency" 					, DownBitCompMethod["SystemClockFrequency"],
				# "\tSystemClockPeriod" 						, DownBitCompMethod["SystemClockPeriod"], 
			# Round Up analyser output 
				# "\tUpDivider"								, DownBitCompMethod["UpDivider"],
				# "\tUpTargetFrequency"						, DownBitCompMethod["UpTargetFrequency"],
				# "\tUpTargetPeriod"							, DownBitCompMethod["UpTargetPeriod"],
				# "\tUpAcquisitionFrequency"					, DownBitCompMethod["UpAcquisitionFrequency"],
				# "\tUpAcquisitionPeriod"						, DownBitCompMethod["UpAcquisitionPeriod"],
				# "\tUpTargetFrequencyError"					, DownBitCompMethod["UpTargetFrequencyError"],
				# "\tUpTargetPeriodError"						, DownBitCompMethod["UpTargetPeriodError"],
				# "\tUpAcquisitionFrequencyError"				, DownBitCompMethod["UpAcquisitionFrequencyError"],
				# "\tUpAcquisitionPeriodError"				, DownBitCompMethod["UpAcquisitionPeriodError"],
				# "\tUpTargetFrequencyRelativeError"			, DownBitCompMethod["UpTargetFrequencyRelativeError"],
				# "\tUpTargetPeriodRelativeError"				, DownBitCompMethod["UpTargetPeriodRelativeError"],
				# "\tUpAcquisitionFrequencyRelativeError"		, DownBitCompMethod["UpAcquisitionFrequencyRelativeError"],
				# "\tUpAcquisitionPeriodRelativeError"		, DownBitCompMethod["UpAcquisitionPeriodRelativeError"],	
			# Round Down analyser output
				# "\tDownDivider"								, DownBitCompMethod["DownDivider"],
				# "\tDownTargetFrequency"						, DownBitCompMethod["DownTargetFrequency"],
				# "\tDownTargetPeriod"						, DownBitCompMethod["DownTargetPeriod"],
				# "\tDownAcquisitionFrequency"				, DownBitCompMethod["DownAcquisitionFrequency"],
				# "\tDownAcquisitionPeriod"					, DownBitCompMethod["DownAcquisitionPeriod"],
				# "\tDownTargetFrequencyError"				, DownBitCompMethod["DownTargetFrequencyError"],
				# "\tDownTargetPeriodError"					, DownBitCompMethod["DownTargetPeriodError"],
				# "\tDownAcquisitionFrequencyError"			, DownBitCompMethod["DownAcquisitionFrequencyError"],
				# "\tDownAcquisitionPeriodError"				, DownBitCompMethod["DownAcquisitionPeriodError"],
				# "\tDownTargetFrequencyRelativeError"		, DownBitCompMethod["DownTargetFrequencyRelativeError"],
				# "\tDownTargetPeriodRelativeError"			, DownBitCompMethod["DownTargetPeriodRelativeError"],
				# "\tDownAcquisitionFrequencyRelativeError"	, DownBitCompMethod["DownAcquisitionFrequencyRelativeError"],		
				# "\tDownAcquisitionPeriodRelativeError"		, DownBitCompMethod["DownAcquisitionPeriodRelativeError"],
			# Compensate Output
				"\tCompMethod" 								, DownBitCompMethod["CompMethod"],
				"\tCompUpNumber" 							, DownBitCompMethod["CompUpNumber"],
				"\tCompDownNumber"							, DownBitCompMethod["CompDownNumber"],
				"\tCompTargetFrequency" 					, DownBitCompMethod["CompTargetFrequency"],
				"\tCompTargetPeriod" 						, DownBitCompMethod["CompTargetPeriod"],
				# "\tCompAcquisiteFrequency" 					, DownBitCompMethod["CompAcquisiteFrequency"],
				# "\tCompAcquisitePeriod" 					, DownBitCompMethod["CompAcquisitePeriod"],
				"\tCompTargetFrequencyError" 				, DownBitCompMethod["CompTargetFrequencyError"],
				"\tCompTargetPeriodError" 					, DownBitCompMethod["CompTargetPeriodError"],
				# "\tCompAcquisiteFrequencyError" 			, DownBitCompMethod["CompAcquisiteFrequencyError"],
				# "\tCompAcquisitePeriodError" 				, DownBitCompMethod["CompAcquisitePeriodError"],
				"\tCompTargetFrequencyRelativeError" 		, DownBitCompMethod["CompTargetFrequencyRelativeError"],
				# "\tCompTargetPeriodRelativeError" 			, DownBitCompMethod["CompTargetPeriodRelativeError"],
				# "\tCompAcquisiteFrequencyRelativeError" 	, DownBitCompMethod["CompAcquisiteFrequencyRelativeError"],
				# "\tCompAcquisitePeriodRelativeError" 		, DownBitCompMethod["CompAcquisitePeriodRelativeError"],
				"\t"	
        	)
    # pass