from fastapi import FastAPI
import subprocess

app = FastAPI()

def _safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return True
    except subprocess.CalledProcessError as e:
        print(e.output)
        return False

def safe_host_input(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = safe_host_input(host.replace(' ', ''))
        if not _safe_ping(safe_host):
            return {'status': 'failed', 'error': 'Invalid input'}
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}