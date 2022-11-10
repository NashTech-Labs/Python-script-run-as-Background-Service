# Short Description about this template
This template help to run python script as a background service.

* In this template we are checking Resident Set Size (rss) memory of any given process  and send the memory size in cloud watch metric in interval of 15 Second.   For that i am using `Systemd`  to run as background service for particular interval and boto3 for send data to the cloudwatch metric.      
# Steps for Execution 

1. `sudo vi /etc/systemd/system/pulse.service`     

here `pulse.service` is the service file.
 

2. `sudo systemctl daemon-reload`

3. `sudo systemctl enable pulse.service`

   This command will create a symlink

4. `sudo systemctl start pulse.service`

This command is used for start the service.

5. `sudo systemctl status pulse.service`
Thhis command is used for check the service is running or not