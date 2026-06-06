from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, text=True)
    return {'status': 'completed'}