from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['8.8.8.8', '127.0.0.1']  # Define a list of allowed hosts
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}