# this module help to find out all div choice
from BaudrateDivider import BaudrateDivider
import math
def BaudrateDivSelect(baud,clk):
    n = 0
    div_list = []
    for n in range(0,15):
    	div_temp = BaudrateDivider(baud,n,clk)
    	div_rela_err = div_temp["relative_baud_error"]
    	if math.fabs(div_rela_err) <= 0.05:
    		div_list.append(div_temp)
    		# pass
        # pass
    # pass
    return div_list
    pass