from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: list):
        result = subprocess.run(command, check=True, shell=False)
        return result

global safe_subprocess
safe_subprocess = SafeSubprocess()

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to escape any special characters in the host
    safe_subprocess.run(command)
    return {"status": "completed"}