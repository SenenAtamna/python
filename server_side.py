import time

error_counter = 0
info_counter = 0
warn_counter = 0 

with open("/home/ubuntu/linux/syslog") as syslog_file:
    syslog = syslog_file.readlines()
    


for line in syslog:
    if " ERROR EC2RoleProvider" in line:
        error_counter += 1
    elif " INFO EC2RoleProvider" in line:
        info_counter += 1
    elif " WARN EC2RoleProvider" in line:
        warn_counter += 1


print(time.time())
print(error_counter)
print(info_counter)
print(warn_counter)            
