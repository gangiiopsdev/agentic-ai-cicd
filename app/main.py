from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.Popen instead of subprocess.call and without shell=True
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_host(host: str):
    return ping(host)