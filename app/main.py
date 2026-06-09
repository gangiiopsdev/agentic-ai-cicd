from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.strip():
        return False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)