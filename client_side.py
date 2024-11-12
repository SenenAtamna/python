from SshToServer import SshToServer
import pandas as pd
import time
import os


placemet = os.getcwd()
my_ssh = SshToServer(r"C:\SINEEN\phyton\homwork\linux\my-key-pair.pem", "54.92.203.220", "ubuntu")
all_logs = my_ssh.runRemoteCommand("python3 /home/ubuntu/linux/server_side.py")

all_log_in_local = all_logs[0].split("\n")
print(all_log_in_local)
time = all_log_in_local[0]
error = all_log_in_local[1]
info = all_log_in_local[2]
warn = all_log_in_local[3]

all_log_info = {"time": [time],
                "ERROR": [error],
                "INFO": [info],
                "WARN": [warn]
                }


df = pd.DataFrame.from_dict(all_log_info)
df.to_csv(placemet + "/data.csv")
