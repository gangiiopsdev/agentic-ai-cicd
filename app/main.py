from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Add your allowed hosts here
    if host in allowed_hosts:
        return True
    return False@app.get("/")def home():
    return {"message": "Agentic Self-Healing Pipeline"}@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'error': 'Host not allowed'}