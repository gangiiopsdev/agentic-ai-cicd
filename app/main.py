from fastapi import FastAPI
import subprocess
generics = 'ping -c 1 {}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}