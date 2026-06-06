from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if not host or not host.isalnum():
        return "Invalid hostname"
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout