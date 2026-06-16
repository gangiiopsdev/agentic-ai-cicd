from fastapi import FastAPI
import shlex
from subprocess import Popen, PIPE

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "output": result[0]}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}