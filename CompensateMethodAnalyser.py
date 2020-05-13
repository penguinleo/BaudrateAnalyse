from DividerAnalyser import DividerAnalyser
div = 7
divider_info = DividerAnalyser(115200,div,40)
divider0_info = DividerAnalyser(115200,0,40)
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
print(divider_info)
print(divider0_info)