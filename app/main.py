from fastapi import FastAPI
import subprocess

app = FastAPI()

generate_random_payload = 'ping {host}'

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(generate_random_payload.format(host=host).split(), shell=False)
    return {'status': 'completed'}