from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with check=False and capture_output=True
    result = subprocess.run(['ping', '-c', '1', host], check=False, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode(), 'stderr': result.stderr.decode()}

global app
app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)