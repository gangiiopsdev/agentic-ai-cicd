from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or ' ' in host:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)