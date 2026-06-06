from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation for demonstration purposes
    return host.startswith('192.168.') or host == 'localhost'

@app.get="/"
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
async def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}