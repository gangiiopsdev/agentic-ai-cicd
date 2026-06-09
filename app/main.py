from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.net']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Host not allowed')
app = FastAPI()
@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)