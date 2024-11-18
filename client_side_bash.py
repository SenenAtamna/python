from SshToServer import SshToServer
import pandas as pd
import time
import os


my_ssh = SshToServer(r"C:\SINEEN\phyton\homwork\linux\my-key-pair.pem", "54.92.203.220", "ubuntu")
file_name = input("Enter File Name : ")
second_to_wait = input("Enter The second To Wait :")
path = ("./linux/bash/bash.sh " + file_name + " " + second_to_wait)
out= my_ssh.runRemoteCommand(path)
print(out[0])





