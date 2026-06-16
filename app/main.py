from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    subprocess.run(['ping', '-c 1', safe_host], check=True)
    return {'status': 'completed'}