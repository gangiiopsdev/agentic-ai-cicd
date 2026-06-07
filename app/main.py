from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)