import os
import re


#live Cell = L
#Dead Cell = D
#size = 25*25 (lengths*widths)

def get_live_count(length,width,input_val):
    live_count = 0
    for x in range(length-1,length+1):
        for y in range(width-1,width+1):
            if x<=length and y<=width and (x!= length or y != width) and input_val[x][y] == "L":
                live_count += 1
    return live_count

lengths = 0
widths = 0
input_val = [[]]
output = [["D" for x in range(lengths)] for y in range(widths)]

for length in range(lengths):
    for width in range(widths):
        live_count = 0
        cur_cell_val = input_val[length][width]

        live_count = get_live_count(length,width,input_val)

        if (cur_cell_val == "L" and live_count<2) or (cur_cell_val == "L" and live_count > 3):
            output[length][width] = "D"
        elif (cur_cell_val == "L" and live_count in [2,3]) or (cur_cell_val == "D" and live_count == 3):
            output[length][width] = "L"
        else:
            output[length][width] = input_val[length][width]

print(output)