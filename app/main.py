from fastapi import FastAPI
import re
import subprocess
def ping(host: str):
    # Sanitize host input to avoid shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
app = FastAPI()
@app.get('/ping')
def ping_endpoint(host: str): return ping(host)