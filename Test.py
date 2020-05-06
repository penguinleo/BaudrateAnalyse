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
for index in range(0,len(baud_info_list)):
	baud_list.append(baud_info_list[index]["baudrate"])
	error_list.append(baud_info_list[index]["baudrate error"])
	pass
fig = plt.figure("error")
plt.plot(baud_list,error_list,'r*')
plt.xlabel("baudrate")
plt.ylabel("error")
plt.show()