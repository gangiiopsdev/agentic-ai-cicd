from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: ['ping', '-c', '4', host]

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(generate_ping_command(shlex.quote(host)), check=True)
    return {'status': 'completed'}