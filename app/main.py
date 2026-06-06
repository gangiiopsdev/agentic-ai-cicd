from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Add a list of allowed hosts
    if host in allowed_hosts:
        try:
            args = shlex.split('ping {}'.format(host))
            result = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": result.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "output": e.output.decode()}
    else:
        return {"status": "error", "output": "Host not allowed"}