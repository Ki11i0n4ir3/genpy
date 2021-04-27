#!/usr/bin/python3

import os
import re
import sys
import subprocess


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


banner = """

 ,:::::,  :::::: ::::  :: ::::::, ::    ::
::        ::     :: :: :: ::    ; ::    ::
::  ::::: :::::  ::  :::: ::::::'  ::  ::
::    ::  ::     ::   ::: ::         ::
':::::::  :::::: ::    :: ::         ::

Automaticaly generate the python3 scripts format for pwn
[!]Name is exploit.py to static

"""
print(bcolors.GREEN)
print(banner)
print(bcolors.ENDC)
usage = """

usage: genpy <binary_name> <remote_host> <port> 

example: genpy a.out vuln.com 1337 

"""

if len(sys.argv) != 4:
    print(bcolors.FAIL)
    print("[!]Need Args")
    print(usage)
    print(bcolors.ENDC)
    sys.exit()


bin_name = sys.argv[1]
remote_host = sys.argv[2]
remote_port = sys.argv[3]

os.system("touch exploit.py")

os.system("chmod +x exploit.py")

print(bcolors.GREEN)
print("[+]Generating the Script...")
print(bcolors.ENDC)

f = open("exploit.py","w")
f.write("#!/usr/bin/python3\n\n")
f.write("from pwn import *\n")

init_state = f"""
#Info:
#
#Deffault : p = process("./{bin_name}")
#If you use to remote, then change the Comment out line
#
#
#SecurityInfo:
#
"""

try:

    sec_info = subprocess.getoutput(f"checksec {bin_name}")
    sec_info = sec_info.split("\n")
    note = ""

    for i in sec_info:

        note += "#" + i+"\n"
    
    init_state += note

    f.write(f"{init_state}\n")

    file_cmd = subprocess.getoutput(f"file {bin_name}")
    file_cmd = file_cmd.split(",")



    for i in file_cmd:

        f.write("#"+i+"\n")

    f.write("\n\n")


except:
    print(bcolors.FAIL)
    print("[!]Maybe Something wrong...")
    print(f"[!]{bin_name}: NotFound")
    print(bcolors.ENDC)
    sys.exit()

#f.write("#!/usr/bin/python3\n\n")
#f.write("from pwn import * \n\n\n")
f.write("p = process(\""+"./"+bin_name+"\")\n")
f.write(f"#p = remote(\"{remote_host}\",{remote_port})\n")
f.write("p.clean()\n\n")

f.close()

print(bcolors.GREEN)
print("[+]Generated The Script")
phase = input("press any key")
print(bcolors.ENDC)

print(bcolors.YELLOW)
print("+--------------+")
print("|format preview|")
print("+--------------+")

f = open("exploit.py","r")

preview_array  = []
preview_array2 = []

for i in f:

    preview_array.append(i)

for i in preview_array:

    preview_array2.append(i.replace("\n",""))

del preview_array

counter = 0

for i in preview_array2:

    if counter <= len(i):
        counter = len(i)

max_length = "+"+"-"*counter+"+"

print(max_length)

for i in preview_array2:
    padding = counter - len(i)
    print("|"+i+" "*padding+"|")

print(max_length)





print(bcolors.ENDC)
