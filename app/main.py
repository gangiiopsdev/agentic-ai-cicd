from fastapi import FastAPI
import subprocess
import re

# Define a regular expression pattern to allow only valid hostnames/IP addresses
ALLOWED_HOSTS_PATTERN = re.compile(r'^\b(127\.0\.0\.1|localhost)$')

def safe_ping(host: str):
    if not ALLOWED_HOSTS_PATTERN.match(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not ALLOWED_HOSTS_PATTERN.match(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)