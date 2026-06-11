from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['192.168.1.1', '10.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        return {'status': 'banned'}
    try:
        subprocess.run(['ping', '--', host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {'status': str(e)}