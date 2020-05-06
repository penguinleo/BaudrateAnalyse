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
for index in range(0,len(baud_info_list)):
	baud_list.append(baud_info_list[index]["baudrate"])
	uplimit_list.append(baud_info_list[index]["baudrate"]*0.003)
	downlimit_list.append(baud_info_list[index]["baudrate"]*(-0.003))
	error_list.append(baud_info_list[index]["baudrate error"])
	pass
fig = plt.figure("error")
plt.plot(baud_list,error_list,'b*')
plt.plot(baud_list,downlimit_list,'r')
plt.plot(baud_list,uplimit_list,'r')
plt.xlabel("baudrate")
plt.ylabel("error")
plt.show()