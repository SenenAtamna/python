#!/bin/bash


for second in $(seq 1 $2)
do
	if [ -e /home/ubuntu/linux/bash/$1 ]
	then
		echo "File $1 Arrived in server in $second second"
		exit 0
	fi
sleep 1
done
echo "Timeout"
