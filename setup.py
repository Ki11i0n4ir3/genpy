#!/usr/bin/python3
import os
import sys

if os.getuid() != 0:
    print("[!]You must execute as root!!!!")
    sys.exit()


step1 = "chmod +x genpy.py"

step2 = "mv genpy.py /usr/bin/genpy"

os.system(step1)

os.system(step2)

print("[+]Done...")
