from fastapi import FastAPI
import subprocess
cimport os

def execute_ping(host: str):
    if not host:
        return False
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    if isinstance(result, bool) and not result:
        return {'status': 'failed'}
    else:
        return {'status': 'completed', 'output': result}