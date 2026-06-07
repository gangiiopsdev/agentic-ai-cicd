from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list for args and shell=False to prevent command injection
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get('/ping')
def ping(host: str):
    return {'status': 'Pinging', 'host': host}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}