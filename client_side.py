from SshToServer import SshToServer
import pandas as pd
import time
import os

def append_to_csv(file_path, data):
    df_new = df = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_csv(file_path, index=False)


file_location = ((os.getcwd()) + "/data.csv")
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

append_to_csv(file_location, all_log_info)


