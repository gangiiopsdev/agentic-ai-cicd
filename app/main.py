from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False to mitigate command injection
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}