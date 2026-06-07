from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Using check_output to avoid shell=True and capture output
        result = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)