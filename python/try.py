#!/usr/local/bin/python

import os
import os.path
root = "./"

for subFolder in os.listdir(root):    
    if os.path.isdir(subFolder) and subFolder!="111":
	    for content in os.listdir(subFolder):
	        os.rename(subFolder+"/"+content, "111/"+content)
			