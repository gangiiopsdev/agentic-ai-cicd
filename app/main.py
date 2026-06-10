from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    escaped_host = shlex.quote(host)
    subprocess.run(['ping', escaped_host], check=True, capture_output=True, text=True)

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to escape shell injection and subprocess.run for better security
    safe_ping(host)
    return {'status': 'completed'}