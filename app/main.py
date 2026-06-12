from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Use parameterized queries or prepared statements instead of string concatenation
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)