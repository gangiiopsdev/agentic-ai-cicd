from fastapi import FastAPI
import subprocess
def ping_host(host):
    cmd = ['ping', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout