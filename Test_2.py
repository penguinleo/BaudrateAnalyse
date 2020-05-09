# 	we should consider a byte as a cycle, not just the bit sending 
# 	In the Test.py we could know that the maximum baudrate error of 
# one bit could be described by the formula 1/(2N-1). The N is the 
# clock number in a bit period. The error is analysed with single 
# bit. But actually the data are sent byte by byte. The start bit 
# of every byte is acting as the sychronize bit. Thus the byte error
# should be considered. Especially the last bit error. 
# 	Compensation method should consider all bits in a byte.
#	Taget:
# 		1. Every acquisition point time error should be less than 6%,
# 	Note that the error should be the single bit error, desperated from
# 	the byte.
# 		2. The last acquisition point time error, or we defined it as
# 	cumulative error, should be less than 3%. More strinctly defining, 
# 	the cumulative error of each bit in the byte should be less than 3%
from BaudCalculate import BaudCalculate
from BaudAnalyse import BaudAnalyse
from BaudrateDivider import BaudrateDivider
from BaudrateDivSearch import BaudrateDivSelect
from SerialDataGenerate import SerialSendWave
from ByteTimeStampAnalyse import ByteTimeStampAnalyse
import matplotlib.pyplot as plt 

baud = 115200
clk1 = 147.456
clk = 40
div = 8
bit_list=ByteTimeStampAnalyse(baud,1,clk1,170)
print(bit_list)
