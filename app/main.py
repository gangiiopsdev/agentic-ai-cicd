from fastapi import FastAPI
import subprocess
from shlex import quote as safe_quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = safe_quote(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}