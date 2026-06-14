from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str) -> dict:
    if host in ['localhost', '127.0.0.1']:  # Add more allowed hosts as needed
        return {'status': 'failed', 'message': f'Pinging {host} is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)