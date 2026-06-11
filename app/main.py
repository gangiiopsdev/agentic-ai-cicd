from fastapi import FastAPI
import subprocess
import shlex
global hosts_cache = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in hosts_cache:
        try:
            subprocess.run(shlex.split(f'ping {host}'), check=True)
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
        else:
            hosts_cache.add(host)
    return {'status': 'completed'}