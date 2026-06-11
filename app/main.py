from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if 'localhost' not in host and '127.0.0.1' not in host:
        return "Invalid host"
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}