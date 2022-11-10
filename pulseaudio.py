import os
import sys
import psutil

import boto3

def checkmemory(pname):
    for id in psutil.pids():
        # if id==pid:
        p = psutil.Process(id)
        if ( p.name() == pname ):
            print(pname) 
            mem = p.memory_info()
            print(mem)
            res=mem[0]
            print ("Memory Perentage of  Resident Set Size is " + str(res))

            cloudwatch = boto3.client('cloudwatch',region_name='us-east-2')
            # Put custom metrics
            cloudwatch.put_metric_data(
                MetricData=[
                    {
                        'MetricName': 'Metric1.2', 
                        'Dimensions': [
                            {
                                'Name': pname,
                                'Value': 'memory usage percent of pulse'
                                
                            },
                            
                        ],
                        'Unit': 'Bytes',
                        'Value': res
                        
                    },
                ],
                Namespace='Test1'
            )

checkmemory('pulseaudio')   // here you can pass any process name that you want to check rss.


