from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex for argument splitting
    args = shlex.split('ping ' + host)
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}