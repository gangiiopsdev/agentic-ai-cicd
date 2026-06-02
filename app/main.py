from fastapi import FastAPI
import subprocess
generate_ping_command = lambda h: ['ping', h]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    subprocess.run(generate_ping_command(host), shell=False)

    return {'status': 'completed'}