from fastapi import FastAPI
import subprocess
glances = [host for host in (os.environ['ALLOWED_HOSTS'].split(','))]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in glances:
        subprocess.call(f'ping {host}')
    else:
        return {'status': 'invalid_host'}
    return {"status": "completed"}