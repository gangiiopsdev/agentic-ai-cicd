from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent command injection
    host = ''.join(filter(str.isalnum, host))
    if len(host) > 0:
        subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}

@app.get="/"
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get="/ping"
def ping(host: str):
    return safe_ping(host)