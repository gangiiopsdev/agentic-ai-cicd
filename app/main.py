from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import os

cmd = ['ping', cmd_quote(host)]
if not validate_host(host):
    raise ValueError('Invalid host name')

# Use os.system or subprocess.call with shell=False to avoid command injection
os.system(' '.join(cmd))
return {'status': 'completed'}