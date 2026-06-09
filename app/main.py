from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if not host or not host.isalnum():
        return "Invalid hostname"
    try:
        cmd = ['ping', host]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)