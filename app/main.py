from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape host
    from shlex import quote
    command = ['ping', quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)