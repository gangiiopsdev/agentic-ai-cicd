from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def wrapper_ping(host: str):
    return ping(host)