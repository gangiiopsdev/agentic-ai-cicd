from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)