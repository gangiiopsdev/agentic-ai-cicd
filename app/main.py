from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with argument quoting to prevent shell injection
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}