from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a safe method to execute external commands
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}