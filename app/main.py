from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', host], shell=False, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed: {e.returncode}")

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping_fixed(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', host], shell=False, check=True)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ping failed: {e.returncode}")