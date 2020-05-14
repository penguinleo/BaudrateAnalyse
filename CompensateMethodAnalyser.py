from DividerAnalyser import DividerAnalyser
from BitCompensateMethodAnalyser import BitCompensateMethodAnalyser
div = 7
divider_info = DividerAnalyser(115200,div,40)
divider0_info = DividerAnalyser(115200,0,40)
comp0 = BitCompensateMethodAnalyser(115200,div,40,0x44)
print("No Divider",
		divider0_info["UpTargetPeriodError"],
		divider0_info["DownTargetPeriodError"])

bits_number_in_byte = 11
acq_number_in_bit = div + 1
Up_Number = 3
Down_Number = acq_number_in_bit - Up_Number
Accumulate_Err_Up_Bit 		= acq_number_in_bit * divider_info["UpAcquisitionPeriodError"]
Accumulate_Err_Down_Bit		= acq_number_in_bit * divider_info["DownAcquisitionPeriodError"]
Accumulate_Err_Compen_Bit 	= Up_Number * divider_info["UpAcquisitionPeriodError"] + Down_Number * divider_info["DownAcquisitionPeriodError"]
print(Accumulate_Err_Up_Bit)
print(Accumulate_Err_Compen_Bit)
print(Accumulate_Err_Down_Bit)
# print(divider_info)
# print(divider0_info)


print('\n',
# The Require frequency infomation
	"The Require frequency infomation",'\n',
	"TargetFrequency", 						':' , comp0["TargetFrequency"], 						'\n',
	"TargetPeriod", 						':' , comp0["TargetPeriod"], 							'\n',
	"AcquisitionDivider", 					':' , comp0["AcquisitionDivider"], 						'\n',
	"AcquisitionFrequency", 				':' , comp0["AcquisitionFrequency"], 					'\n',
	"AcquisitionPeriod", 					':' , comp0["AcquisitionPeriod"], 						'\n',
	"SystemClockFrequency", 				':' , comp0["SystemClockFrequency"], 					'\n',
	"SystemClockPeriod", 					':' , comp0["SystemClockPeriod"], 						'\n',
# Round Up analyser output 
	"\n",
	"Round Up Analyser Output \n",
	"UpDivider", 							':' , comp0["UpDivider"], 								'\n',   
	"UpTargetFrequency", 					':' , comp0["UpTargetFrequency"], 						'\n',   
	"UpTargetPeriod", 						':' , comp0["UpTargetPeriod"], 							'\n',   
	"UpAcquisitionFrequency", 				':' , comp0["UpAcquisitionFrequency"], 					'\n',   
	"UpAcquisitionPeriod", 					':' , comp0["UpAcquisitionPeriod"], 					'\n',   
	"UpTargetFrequencyError", 				':' , comp0["UpTargetFrequencyError"], 					'\n',   
	"UpTargetPeriodError", 					':' , comp0["UpTargetPeriodError"], 					'\n',   
	"UpAcquisitionFrequencyError", 			':' , comp0["UpAcquisitionFrequencyError"], 			'\n',   
	"UpAcquisitionPeriodError", 			':' , comp0["UpAcquisitionPeriodError"], 				'\n',   
	"UpTargetFrequencyRelativeError", 		':' , comp0["UpTargetFrequencyRelativeError"], 			'\n',   
	"UpTargetPeriodRelativeError", 			':' , comp0["UpTargetPeriodRelativeError"], 			'\n',   
	"UpAcquisitionFrequencyRelativeError", 	':' , comp0["UpAcquisitionFrequencyRelativeError"], 	'\n',   
	"UpAcquisitionPeriodRelativeError", 	':' , comp0["UpAcquisitionPeriodRelativeError"], 		'\n',   	
# Round Down analyser output
	"\n",
	"Round Down Analyser Output \n",
	"DownDivider", 							':' , comp0["DownDivider"], 							'\n', 						
	"DownTargetFrequency", 					':' , comp0["DownTargetFrequency"], 					'\n', 
	"DownTargetPeriod", 					':' , comp0["DownTargetPeriod"], 						'\n', 
	"DownAcquisitionFrequency", 			':' , comp0["DownAcquisitionFrequency"], 				'\n', 
	"DownAcquisitionPeriod", 				':' , comp0["DownAcquisitionPeriod"], 					'\n', 
	"DownTargetFrequencyError", 			':' , comp0["DownTargetFrequencyError"], 				'\n', 
	"DownTargetPeriodError", 				':' , comp0["DownTargetPeriodError"], 					'\n', 
	"DownAcquisitionFrequencyError", 		':' , comp0["DownAcquisitionFrequencyError"], 			'\n', 
	"DownAcquisitionPeriodError", 			':' , comp0["DownAcquisitionPeriodError"], 				'\n', 
	"DownTargetFrequencyRelativeError", 	':' , comp0["DownTargetFrequencyRelativeError"], 		'\n', 
	"DownTargetPeriodRelativeError", 		':' , comp0["DownTargetPeriodRelativeError"], 			'\n', 
	"DownAcquisitionFrequencyRelativeError",':' , comp0["DownAcquisitionFrequencyRelativeError"],	'\n', 
	"DownAcquisitionPeriodRelativeError", 	':' , comp0["DownAcquisitionPeriodRelativeError"], 		'\n', 	
# Compensate Output 
	"\n",
	"Compensate Analyser Output \n",
	"CompMethod" , 							':' , comp0["CompMethod"], 								'\n',
	"CompUpNumber" , 						':' , comp0["CompUpNumber"], 							'\n',
	"CompDownNumber" , 						':' , comp0["CompDownNumber"], 							'\n',
	"RoundUpDivider", 						':' , comp0["UpDivider"], 								'\n',
	"RoundDownDivider", 					':' , comp0["DownDivider"], 							'\n',
	"CompTargetFrequency", 					':' , comp0["CompTargetFrequency"], 					'\n',
	"CompTargetPeriod", 					':' , comp0["CompTargetPeriod"], 						'\n',
	"CompAcquisiteFrequency", 				':' , comp0["CompAcquisiteFrequency"], 					'\n',
	"CompAcquisitePeriod", 					':' , comp0["CompAcquisitePeriod"], 					'\n',
	"CompTargetFrequencyError", 			':' , comp0["CompTargetFrequencyError"], 				'\n',
	"CompTargetPeriodError", 				':' , comp0["CompTargetPeriodError"], 					'\n',
	"CompAcquisiteFrequencyError", 			':' , comp0["CompAcquisiteFrequencyError"], 			'\n',
	"CompAcquisitePeriodError", 			':' , comp0["CompAcquisitePeriodError"], 				'\n',
	"CompTargetFrequencyRelativeError", 	':' , comp0["CompTargetFrequencyRelativeError"], 		'\n',
	"CompTargetPeriodRelativeError", 		':' , comp0["CompTargetPeriodRelativeError"], 			'\n',
	"CompAcquisiteFrequencyRelativeError", 	':' , comp0["CompAcquisiteFrequencyRelativeError"], 	'\n',
	"CompAcquisitePeriodRelativeError", 	':' , comp0["CompAcquisitePeriodRelativeError"],		'\n'
	)