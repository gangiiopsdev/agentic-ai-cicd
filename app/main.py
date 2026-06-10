from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

def safe_ping(host: str):
    try:
        result = sp.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except sp.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sp.run(['ping', host], check=True)
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'