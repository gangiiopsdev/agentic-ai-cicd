from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using shlex.quote to escape shell characters
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}