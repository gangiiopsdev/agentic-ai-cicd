from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['8.8.8.8', '127.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_safe_hosts:
        return {"error": "Invalid host"}, 403

    result = subprocess.call(f'ping {host}', shell=False)
    return {'status': 'completed', 'result': result}