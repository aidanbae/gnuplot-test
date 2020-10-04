import os
import re
import time

def report(c, lines):
    rtv = []
    for str in lines:
        str=re.sub("^[ \t]+",'', str)
        if str.find("Latency") == 0 or str.find("Requests/sec") == 0:
            token = re.split("[ \t]+", str)
            value = re.sub("[^0-9\.]", '', token[1])
            if re.match("[0-9\.]+us", token[1]):
                rtv.append(float(value)/1000)
            elif re.match("[0-9\.]+s", token[1]):
                rtv.append(float(value)*1000)
            else:
                rtv.append(float(value))
    print c,"\t", rtv[0],"\t",rtv[1]

def run(cmd):
    stdin, stdout, stderr = os.popen3(cmd)
    return stdout.readlines()

offset = 5
maxConcurrency = offset * 61
duration = 10
for num in range(1, maxConcurrency/offset):
    concurrency = num * offset
    thread = 16 if concurrency > 16 else concurrency
    cmd = ("wrk -t %d -c %d -d %ds http://localhost:8080" % (thread, concurrency, duration))
    result =run(cmd)
    report(concurrency, result)
    time.sleep(5)