from fastapi import FastAPI
import subprocess
def execute_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for simplicity
        subprocess.call(['ping', host])
    else:
        raise ValueError('Ping to non-localhost is not allowed')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {'error': str(e)}