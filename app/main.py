from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ip_address = subprocess.check_output(['nslookup', host], stderr=subprocess.STDOUT).decode().strip()
        return {'status': 'completed', 'ip_address': ip_address}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)