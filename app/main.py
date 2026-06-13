from fastapi import FastAPI
import subprocess
glances = ['ping', 'google.com']

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with a safe executable path and trusted input
    if host in glances:
        result = subprocess.run(glances, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with a safe executable path and trusted input
    if host in glances:
        result = subprocess.run(glances, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}