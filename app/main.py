from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)