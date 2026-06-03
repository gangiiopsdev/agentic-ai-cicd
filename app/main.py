from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return f'ping {host}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(safe_ping(host), check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode('utf-8')}