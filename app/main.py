from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen and avoiding shell=True
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)