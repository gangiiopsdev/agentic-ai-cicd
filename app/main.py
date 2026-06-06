from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen
    command = ['ping', host]
    subprocess.run(command, capture_output=True, text=True)