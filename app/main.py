from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation using subprocess.run with escaped arguments
    try:
        subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return {'status': 'failed', 'error': result['error']}
    else:
        return {'status': 'completed'}