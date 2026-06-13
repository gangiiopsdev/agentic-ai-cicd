from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    try:
        subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not os.path.exists('/sbin/ping'):  # Check for the presence of ping command
        return {'error': 'Ping command not available'}
    return safe_ping(host)