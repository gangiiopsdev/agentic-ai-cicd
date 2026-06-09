from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.Popen for better security and avoid shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f'Failed to ping {host}: {e.stderr.decode()}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return 'Invalid hostname'
    return safe_ping(host)