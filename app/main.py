from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run and shlex.quote
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'host': host, 'message': 'Please provide a valid hostname'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}