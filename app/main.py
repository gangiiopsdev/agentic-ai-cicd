from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    args = shlex.split(f'ping {host}')
    sanitized_host = subprocess.escape(host)
    sanitized_args = f'ping {sanitized_host}'
    args = shlex.split(sanitized_args)
    subprocess.run(args, check=True)
    return {"status": "completed"}