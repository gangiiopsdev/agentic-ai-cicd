from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define allowed host patterns
ALLOWED_HOSTS = re.compile(r'^\w+$')

def safe_ping(host: str):
    if not ALLOWED_HOSTS.match(host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)