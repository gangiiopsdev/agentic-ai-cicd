from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    if host in ['localhost', '127.0.0.1']:  # Add more allowed hosts as needed
        return f'Pinging {host} is not allowed'
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)