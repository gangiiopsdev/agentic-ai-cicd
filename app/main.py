from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts
        if host in ['localhost', '127.0.0.1']:
            result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        else:
            raise ValueError("Invalid host")
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get="/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}