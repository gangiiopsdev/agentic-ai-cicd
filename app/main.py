from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
import os

cmd = ['ping', cmd_quote(host)]
if not validate_host(host):
    raise ValueError('Invalid host name')

# Use subprocess.call with shell=False to avoid command injection
subprocess.call(cmd, shell=False)
return {'status': 'completed'}