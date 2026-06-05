from fastapi import FastAPI
import subprocess
global_host = 'example.com' # Replace with safe default or user input validation

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', global_host]) # Use list to avoid shell=True and potential injection attacks
    return {'status': 'completed'}