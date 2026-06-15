from fastapi import FastAPI
import subprocess
def execute_safe_ping(host: str):
    # Ensure the host parameter is sanitized and does not contain malicious content
    safe_host = ''.join(filter(str.isalnum, host))
    subprocess.run(['ping', f'"{safe_host}"'], check=True, timeout=5)

global process_pool
process_pool = {}
def ping(host: str):
    if host in process_pool:
        return {'status': 'already running'}
    execute_safe_ping(host)
    process_pool[host] = True
    return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    execute_safe_ping(host)
    return {'status': 'completed'}