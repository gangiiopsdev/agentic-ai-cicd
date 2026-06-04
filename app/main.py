from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400

    # Secure implementation using a fully qualified command path to mitigate shell injection risks
    subprocess.run(["/bin/ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return {"status": "completed"}