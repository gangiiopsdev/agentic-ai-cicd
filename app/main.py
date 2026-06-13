from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with proper argument handling
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}