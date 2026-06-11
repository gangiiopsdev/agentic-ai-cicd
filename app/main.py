from fastapi import FastAPI
import subprocess
global ping_blacklist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    if host not in ping_blacklist:
        subprocess.call(f'ping {host}', shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid host'}

    return {'status': 'completed'}