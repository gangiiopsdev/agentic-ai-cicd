from fastapi import FastAPI
import subprocess
cimport os

def safe_ping(host: str):
    if not all(c in string.ascii_letters + string.digits + '-.' for c in host):
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)