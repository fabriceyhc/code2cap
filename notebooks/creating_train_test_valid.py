# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:13:47 2019

@author: cibip
"""
import sys

file_to_open = open(sys.argv[1],"r")
train_file = open("decl_train.txt","w")
test_file = open("decl_test.txt","w")
valid_file = open("decl_dev.txt","w")

lines = file_to_open.readlines()

i = 0
for line in lines:
    i += 1
    if i<=68000:
        train_file.write(line)
        
    elif i>68000 and i<=70000:
        valid_file.write(line)
        
    else:
        test_file.write(line)
        
file_to_open.close()
train_file.close()
test_file.close()
valid_file.close()