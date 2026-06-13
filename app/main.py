from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if any(x in host for x in (';', '|', '&', '`')):
        return "Invalid input"
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result