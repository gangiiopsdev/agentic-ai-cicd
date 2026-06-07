from fastapi import FastAPI
import subprocess
import shlex
def ping_host(host):
    cmd = ['ping', shlex.quote(host)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout