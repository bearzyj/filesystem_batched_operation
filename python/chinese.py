#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
root = "./"

#ss="听见了吗"
#if ss.startswith( "听 见" ):
#    print ss.decode("utf-8")

for subFolder in os.listdir(root): 
   # if subFolder!="try.py":
   #     print subFolder.decode("cp936")
   #     break 
    if os.path.isfile(subFolder) and subFolder.decode("cp936").encode("utf-8").startswith("听童话故事第"):
	    os.rename(subFolder, "听童话故事 ".decode("utf-8").encode("cp936")+subFolder[10:])
	    #print "听童话故事 ".decode("utf-8").encode("cp936")+subFolder[10:]
