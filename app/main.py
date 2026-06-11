from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        return {'status': 'error', 'message': 'Host is banned'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=False)
        return {"status": "completed", 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.stderr.decode())}