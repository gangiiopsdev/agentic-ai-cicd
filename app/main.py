from fastapi import FastAPI
import subprocess
global_vars = {}

app = FastAPI()

def ping(host: str):
    if 'ping' in host or host.isnumeric():
        cmd = ['ping', host]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return {'status': result.stdout}
    else:
        return {'error': 'Invalid input'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)