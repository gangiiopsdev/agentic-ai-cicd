from fastapi import FastAPI
import subprocess
call = subprocess.run,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    call(['ping', host], check=True)
    return {'status': 'completed'}