from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.stdout}