from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation with validation
    if host.strip().endswith('.localdomain'):
        safe_host = host.replace('.', '_').replace('-', '_')
        subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed'}