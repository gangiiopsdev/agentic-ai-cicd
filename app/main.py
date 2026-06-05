from fastapi import FastAPI
import subprocess
import shlex
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ip_address = socket.gethostbyname(host)
        args = shlex.split(f'ping {ip_address}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, socket.gaierror) as e:
        return {'status': 'failed', 'error': str(e)}