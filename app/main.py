from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    host = subprocess.list2cmdline([host])
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}