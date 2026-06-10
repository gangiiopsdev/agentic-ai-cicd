from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host != 'localhost' and host != '127.0.0.1':
        return {'status': 'failed', 'error': 'Ping to non-localhost hosts is not allowed'}
    args = ["ping", shlex.quote(host)]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(shlex.quote(host))