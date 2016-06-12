# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 04:45:42 2015

@author: rcortez
"""

import subprocess
import os
PATH = "folder Path"
   
for root, dirs, files in os.walk(PATH):
    for f in files:
        if f.endswith('pdf'):            
            fname = os.path.join(root, f)                        
            process = subprocess.Popen(["pdftotext", "-layout", fname], shell=False, 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            content, err = process.communicate()[0:2]
            print fname + '*'*20 + content
            print str(err) + '*'*20 + content

