#   we should consider a byte as a cycle, not just the bit sending 
#   In the Test.py we could know that the maximum baudrate error of 
# one bit could be described by the formula 1/(2N-1). The N is the 
# clock number in a bit period. The error is analysed with single 
# bit. But actually the data are sent byte by byte. The start bit 
# of every byte is acting as the sychronize bit. Thus the byte error
# should be considered. Especially the last bit error. 
#   Compensation method should consider all bits in a byte.
#   Taget:
#       1. Every acquisition point time error should be less than 6%,
#   Note that the error should be the single bit error, desperated from
#   the byte.
#       2. The last acquisition point time error, or we defined it as
#   cumulative error, should be less than 3%. More strinctly defining, 
#   the cumulative error of each bit in the byte should be less than 3%
from BaudCalculate import BaudCalculate
from BaudAnalyse import BaudAnalyse
from BaudrateDivider import BaudrateDivider
from BaudrateDivSearch import BaudrateDivSelect
from SerialDataGenerate import SerialSendWave
from ByteTimeStampAnalyse import ByteTimeStampAnalyse
import matplotlib.pyplot as plt 
from DividerAnalyser import DividerAnalyser
baud = 115200
clk1 = 14.7456
clk = 40
div = 7
# bit_list = ByteTimeStampAnalyse(baud,0,clk1,170)
ByteStampDic        = ByteTimeStampAnalyse(baud,div,clk,170)
print(ByteStampDic["baudrate_info"])
CalculatedStamps    = ByteStampDic["bits_list"]
RoundUpStamps       = ByteStampDic["up_bits_list"]
RoundDownStamps     = ByteStampDic["down_bits_list"]
# divider_info = DividerAnalyser(baud,div,clk)
ref = []
acq = []
acq_list = []
up = []
down =[]
up_acq = []
up_acq_list = []
down_acq = []
down_acq_list = []
up_err = []
down_err = []
up_acq_err = []
down_acq_err = []
up_acq_err_list = []
down_acq_err_list = []
for index in range(0,len(CalculatedStamps)):
    ref.append(CalculatedStamps[index]["BitStartTime"]) 
    acq = acq + CalculatedStamps[index]["AcquisiteStampList"]
    up.append(RoundUpStamps[index]["BitStartTime"])
    down.append(RoundDownStamps[index]["BitStartTime"])
    up_acq  = up_acq + RoundUpStamps[index]["UpAcquisiteStampList"]
    down_acq = down_acq + RoundDownStamps[index]["DownAcquisiteStampList"]
    up_err.append(RoundUpStamps[index]["BitStartTime"] - CalculatedStamps[index]["BitStartTime"])
    down_err.append(RoundDownStamps[index]["BitStartTime"] - CalculatedStamps[index]["BitStartTime"])
    ref.append(CalculatedStamps[index]["BitStopTime"]) 
    up.append(RoundUpStamps[index]["UpBitStopTime"])
    down.append(RoundDownStamps[index]["DownBitStopTime"])
    up_err.append(RoundUpStamps[index]["UpBitStopTime"] - CalculatedStamps[index]["BitStopTime"])
    down_err.append(RoundDownStamps[index]["DownBitStopTime"] - CalculatedStamps[index]["BitStopTime"])
    pass
for index in range(0,len(acq)):
    acq_list.append(acq[index]["AcquisiteStartStamp"])
    acq_list.append(acq[index]["AcquisiteStopStamp"])
    up_acq_list.append(up_acq[index]["AcquisiteStartStamp"])
    up_acq_list.append(up_acq[index]["UpAcquisiteStopStamp"])
    up_acq_err_list.append(up_acq[index]["AcquisiteStartStamp"] - acq[index]["AcquisiteStartStamp"])
    up_acq_err_list.append(up_acq[index]["UpAcquisiteStopStamp"] - acq[index]["AcquisiteStopStamp"])
    down_acq_list.append(down_acq[index]["AcquisiteStartStamp"])
    down_acq_list.append(down_acq[index]["DownAcquisiteStopStamp"])
    down_acq_err_list.append(down_acq[index]["AcquisiteStartStamp"] - acq[index]["AcquisiteStartStamp"])
    down_acq_err_list.append(down_acq[index]["DownAcquisiteStopStamp"] - acq[index]["AcquisiteStopStamp"])
fig = plt.figure("bit stamp time map")
plt.plot(ref,'bo')
plt.plot(up,'r*')
plt.plot(down,'g*')
plt.xlabel("bit stamp index")
plt.ylabel("time stamp / ns")

fig = plt.figure("error of each stamp")
plt.plot(up_err,'b.')
plt.plot(down_err,'r.')
plt.xlabel("bit stamp index")
plt.ylabel("time stamp err / ns")

fig = plt.figure("acquisition stamp")
plt.plot(acq_list,'bo')
plt.plot(up_acq_list,'r*')
plt.plot(down_acq_list,'g*')
plt.xlabel("bit stamp index")
plt.ylabel("time stamp / ns")
plt.grid("on")

fig = plt.figure("acquisition stamp error")
plt.plot(up_acq_err_list,'bo')
plt.plot(down_acq_err_list,'r*')
plt.xlabel("bit stamp index")
plt.ylabel("time stamp error / ns")
plt.grid("on")
plt.show()
# print(bit_list)
# print(ByteStampDic)

# print(divider_info)