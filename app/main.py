from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], capture_output=True, text=True)