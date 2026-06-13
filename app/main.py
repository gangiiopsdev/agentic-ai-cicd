from fastapi import FastAPI
import subprocess
call = subprocess.call
def ping(host: str):
    # Safe implementation
    call(['ping', host])