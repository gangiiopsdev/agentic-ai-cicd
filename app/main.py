from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)