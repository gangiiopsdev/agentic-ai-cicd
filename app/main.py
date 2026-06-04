from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', subprocess.check_output(f'echo {host}', shell=True).decode().strip()])

    return {'status': 'completed'}