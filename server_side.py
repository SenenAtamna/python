import time

error_counter = 0
info_counter = 0
warn_counter = 0 

with open("/home/ubuntu/linux/syslog") as syslog_file:
    syslog = syslog_file.read()
    
syslog_file_in_list = syslog.split('\n')

for line in syslog_file_in_list:
    if "ERROR " in line:
        error_counter += 1
    elif "INFO " in line:
        info_counter += 1
    elif "WARN " in line:
        warn_counter += 1


print(time.time())
print(error_counter)
print(info_counter)
print(warn_counter)            
