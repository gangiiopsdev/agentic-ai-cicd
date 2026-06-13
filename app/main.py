from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}