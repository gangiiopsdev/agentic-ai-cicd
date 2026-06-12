from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    if not host or '&&' in host or ';' in host or '|' in host or '`' in host or '&' in host or '$(' in host or ')$' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = 'ping'
    args = shlex.split(f'{command} {host}')
    try:
        subprocess.run(args, check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result