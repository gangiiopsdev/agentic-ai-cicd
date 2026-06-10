from fastapi import FastAPI
import subprocess
import shlex
import os

cmd = ['ping', host]
if not all(os.path.exists(p) for p in os.uname().nodename.split()):
    raise ValueError('Invalid hostname')
subprocess.call(cmd)
return {'status': 'completed'}