from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation using check_output with shell=False and proper argument handling
    subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
    return {'status': 'completed'}