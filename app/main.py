from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping {host}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}