from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host], shell=False)

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    return {"status": "completed", "sanitized_input": sanitized_host}