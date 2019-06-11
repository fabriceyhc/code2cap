# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:03:36 2019

@author: cibip
"""

import re 
import sys

file_needed = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')
lines = file_needed.readlines()

function_list = []
n = 0

for line in lines:
    
    """
    n+=1 
    if n > 3:
        break
    """
    #print(line)
        
    my_string = line
    if re.search('def [a-z]* [a-z]* ',my_string):
        
        to_remove = re.search('def [a-z]* [a-z]* ',my_string).group(0)
        pr_line = line.replace(to_remove,"")
        #print(pr_line)
    else: 
        to_remove = ""
    #line_str = my_string[ my_string.find("def ")+4 : my_string.find("(") ]
    output_file.write(pr_line)
    #function_list.append(to_remove)

file_needed.close()
output_file.close()


