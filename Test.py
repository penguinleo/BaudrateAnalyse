# According to this module, we can know that the maximum relative error caused by
# the system clock could be calculated by the divider.
# Baudrate = SysClkFreq / DIV
# BitTime = 1/Baudrate = DIV * SysClk + BitErr
# RefErr = BitErr / BitTime
# We could know that the |BitErr| < (SysClk / 2)
# The the |RefErr| < (1 / ( 2 * DIV - 1 ) )
from BaudCalculate import BaudCalculate
from BaudAnalyse import BaudAnalyse
from BaudrateDivider import BaudrateDivider
from BaudrateDivSearch import BaudrateDivSelect
from SerialDataGenerate import SerialSendWave
import matplotlib.pyplot as plt 
baud = 115200
clk = 60
div = 8
baud_info = BaudCalculate(baud,clk)
print(baud_info)
baud_info = BaudrateDivider(baud,div,clk)
print(baud_info)
baud_info_list = BaudAnalyse(clk)
print(len(baud_info_list))
baud_list =[]
error_list = []
uplimit_list = []
downlimit_list = []
relative_err_list = []
bit_time_error = []
# relative_err_list = [0.1] * len(baud_info_list)
uprelative_list = [0.003] * len(baud_info_list)
lowrelative_list = [-0.003] * len(baud_info_list)
up_time_limit_list = []
low_time_limt_list = []
max_relative_err_list = []
min_relative_err_list = []
index = 0
for index in range(0,len(baud_info_list)):
	baud_list.append(baud_info_list[index]["baudrate"])
	uplimit_list.append(baud_info_list[index]["baudrate"]*0.003)
	downlimit_list.append(baud_info_list[index]["baudrate"]*(-0.003))
	error_list.append(baud_info_list[index]["baudrate_error"])
	relative_err_list.append(baud_info_list[index]["relative_baud_error"])
	bit_time_error.append(baud_info_list[index]["bit_time_error"])
	up_time_limit_list.append(baud_info_list[index]["bit_time"]*0.003)
	low_time_limt_list.append(baud_info_list[index]["bit_time"]*(-0.003))
	max_relative_err_list.append(baud_info_list[index]["relative_error_maximum"])
	min_relative_err_list.append(baud_info_list[index]["relative_error_maximum"]*(-1.0))
	pass
div_list = BaudrateDivSelect(baud,clk)
div_n_list = []
div_relat_err_list = []
for index in range(0,len(div_list)):
	div_n_list.append(div_list[index]["BDIV"])
	div_relat_err_list.append(div_list[index]["relative_baud_error"])
	pass
# print(div_list)
fig = plt.figure("baudrate error")
plt.plot(baud_list,error_list,'b*')
plt.plot(baud_list,downlimit_list,'r')
plt.plot(baud_list,uplimit_list,'r')
plt.xlabel("baudrate")
plt.ylabel("error")
# plt.show()
fig2 = plt.figure("relative error")
plt.plot(baud_list,relative_err_list,'b*')
plt.plot(baud_list,uprelative_list,'r')
plt.plot(baud_list,lowrelative_list,'r')
plt.plot(baud_list,max_relative_err_list,'y.')
plt.plot(baud_list,min_relative_err_list,'y.')
plt.xlabel("baudrate")
plt.ylabel("relative")
fig3 = plt.figure("bit time error")
plt.plot(baud_list,bit_time_error,'b*')
plt.plot(baud_list,up_time_limit_list,'r')
plt.plot(baud_list,low_time_limt_list,'r')
plt.xlabel("baudrate")
plt.ylabel("bit time error /ns")
fig4 = plt.figure("baud div relative error")
plt.plot(div_n_list,div_relat_err_list,'b*')
plt.xlabel("DIV")
plt.ylabel("relative error")
plt.title("baud div relative error")

wave_list = []
wave_value = []
wave_time = []
wave_value_B = []
wave_time_B = []
wave_info = SerialSendWave(115200,14.7456,170)
wave_info_B = SerialSendWave(115200,40,170)
wave_list = wave_info["Wave Data List"]
wave_list_B = wave_info_B["Wave Data List"]
for index in range(0,len(wave_list)):
	wave_value.append(wave_list[index]["Value"])
	wave_time.append(wave_list[index]["Time"])
	pass
for index in range(0,len(wave_list_B)):
	wave_value_B.append(wave_list_B[index]["Value"])
	wave_time_B.append(wave_list_B[index]["Time"])
	pass
fig5 = plt.figure("baudrate wave")
plt.plot(wave_time,wave_value,'b*')
plt.plot(wave_time_B,wave_value_B,'r.')
plt.show()


