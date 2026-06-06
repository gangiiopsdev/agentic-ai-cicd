from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    try:
        args = ['ping', shlex.quote(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it's a valid IP address or hostname
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    domain_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not (ip_pattern.match(host) or domain_pattern.match(host)):
        return {'error': 'Invalid input'}
    return safe_ping(host)