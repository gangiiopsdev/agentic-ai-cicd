from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in globally_allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}