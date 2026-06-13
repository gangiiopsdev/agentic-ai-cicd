from fastapi import FastAPI
import subprocess
import shlex
import os

cmd = ['ping', host]
if not all(os.path.basename(p).isalnum() for p in cmd):
    return {'error': 'Invalid input'}
subprocess.call(cmd)
return {'status': 'completed'}