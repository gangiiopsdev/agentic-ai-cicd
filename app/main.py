from fastapi import FastAPI
import subprocess
import shlex

cmd = ['ping', '-c', '4'] + shlex.split(host)
subprocess.call(cmd, shell=False)  # Use a specific number of pings for security
return {'status': 'completed'}