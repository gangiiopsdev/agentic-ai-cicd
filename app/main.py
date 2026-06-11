from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], shell=False, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Example of input validation
        return {'status': 'failed', 'error': 'Invalid host name'}
    safe_ping_command = ['ping', subprocess.quote(host)]  # Sanitize the host input
    try:
        output = subprocess.check_output(safe_ping_command, shell=False, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}