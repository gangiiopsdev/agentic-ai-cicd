from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration purposes
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Ping to non-localhost hosts is not allowed.'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}