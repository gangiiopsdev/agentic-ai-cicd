from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    await safe_ping(host)
    return {'status': 'completed'}