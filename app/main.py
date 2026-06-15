from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return [part.strip() for part in host.split() if part.strip().isalnum()]

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping'] + safe_ping(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}