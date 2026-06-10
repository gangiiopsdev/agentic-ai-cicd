from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
        if host not in allowed_hosts:
            raise ValueError(f'Host {host} is not allowed')
        command = ['ping', host]
        args = shlex.split(' '.join(command))
        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}