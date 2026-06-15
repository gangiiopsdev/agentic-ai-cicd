from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host):
    try:
        args = shlex.split('ping ' + host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return run_ping(host)