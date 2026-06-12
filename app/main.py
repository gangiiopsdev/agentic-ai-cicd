from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    result = subprocess.run(['/bin/ping', *shlex.split(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    result = subprocess.run(['/bin/ping', *shlex.split(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}