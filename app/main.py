from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}