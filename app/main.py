from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if 'ping' in host or host.startswith('-'):
        return "Invalid input"
    result = subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)