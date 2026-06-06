from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}