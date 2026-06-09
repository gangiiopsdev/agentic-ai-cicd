from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}