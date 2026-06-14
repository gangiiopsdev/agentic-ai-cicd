from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize user input to prevent command injection
    host = ''.join(char for char in host if char.isalnum() or char in ['.', '-', '_'])
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}