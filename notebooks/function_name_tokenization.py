# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:23:45 2019

@author: cibip
"""

import re 
import sys

file_needed = open(sys.argv[1],"r")
output_file = open(sys.argv[2],"w")
lines = file_needed.readlines()

function_list = []
n = 0

for line in lines:
    
    """
    n+=1 
    if n > 12:
        break
    """
    
    my_string = line
    if re.search(r'def (.*?)\(', my_string):
        req_string = re.search(r'def (.*?)\(', my_string).group(1)
    else: 
        req_string = " "
    #line_str = my_string[ my_string.find("def ")+4 : my_string.find("(") ]
    function_list.append(req_string)

tokenized_function_list = []
for ele in function_list:
    curr_ele = re.sub("_", " ", ele)
    
    curr_ele = re.sub(r"(?<=\w)([A-Z])", r" \1", curr_ele)
    tokenized_function_list.append(curr_ele.lower())
    output_file.write(curr_ele.lower().lstrip()+"\n")
    
file_needed.close()
output_file.close()
