from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with check=False and capture_output=True
    result = subprocess.run(['ping', host], check=False, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode(), 'stderr': result.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)