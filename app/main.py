from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and shell=False
    subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}