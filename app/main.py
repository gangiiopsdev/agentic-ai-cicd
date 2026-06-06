from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], capture_output=True, text=True)