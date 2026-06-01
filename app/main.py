from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}