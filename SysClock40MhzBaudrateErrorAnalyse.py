# According to this module, we can know that the maximum relative error caused by
# the system clock could be calculated by the divider.
# Baudrate = SysClkFreq / DIV
# BitTime = 1/Baudrate = DIV * SysClk + BitErr
# RefErr = BitErr / BitTime
# We could know that the |BitErr| < (SysClk / 2)
# The the |RefErr| < (1 / ( 2 * DIV - 1 ) )
from BaudCalculate import BaudCalculate
from BaudAnalyse import BaudAnalyse
import matplotlib.pyplot as plt 

baud = 115200
clk = 40
baud_info = BaudCalculate(baud,clk)
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
    # relative_err_list.append(baud_info_list[index]["baudrate"])
    # # uprelative_list.append(0.003)
    # lowrelative_list.append(-0.003)
	pass
fig = plt.figure("baudrate error")
plt.plot(baud_list,error_list,'b*')
plt.plot(baud_list,downlimit_list,'r')
plt.plot(baud_list,uplimit_list,'r')
plt.xlabel("baudrate/bps")
plt.ylabel("error/bps")
# plt.show()
fig2 = plt.figure("relative error")
plt.plot(baud_list,relative_err_list,'b*')
plt.plot(baud_list,uprelative_list,'r')
plt.plot(baud_list,lowrelative_list,'r')
plt.plot(baud_list,max_relative_err_list,'y.')
plt.plot(baud_list,min_relative_err_list,'y.')
plt.xlabel("baudrate/bps")
plt.ylabel("relative")

fig3 = plt.figure("bit time error")
plt.plot(baud_list,bit_time_error,'b*')
plt.plot(baud_list,up_time_limit_list,'r')
plt.plot(baud_list,low_time_limt_list,'r')
plt.xlabel("baudrate/bps")
plt.ylabel("bit time error /ns")
plt.show()