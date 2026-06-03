from fastapi import FastAPI
import subprocess
def ping_host(host):
    call_args = ['ping', host]
    result = subprocess.run(call_args, capture_output=True, text=True)
    return result.stdout