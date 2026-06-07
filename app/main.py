from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1'] + shlex.split(host), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)