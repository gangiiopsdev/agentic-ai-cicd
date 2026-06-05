from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {'example.com', 'localhost'}

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    if host in globally_allowed_hosts:
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        raise ValueError('Host not allowed')