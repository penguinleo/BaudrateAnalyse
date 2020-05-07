# this module help to find out all div choice
from BaudrateDivider import BaudrateDivider
def BaudrateDivSelect(baud,clk):
    n = 0
    div_list = []
    for n in range(0,15):
        div_list.append(BaudrateDivider(baud,n,clk))
        pass
    return div_list
    pass