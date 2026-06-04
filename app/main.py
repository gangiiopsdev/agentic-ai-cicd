from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    return execute_ping(host)

def is_valid_host(host):
    # Implement validation logic here, e.g., checking for allowed domains/IPs
    return True