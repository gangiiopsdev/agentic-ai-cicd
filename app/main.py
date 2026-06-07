from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)