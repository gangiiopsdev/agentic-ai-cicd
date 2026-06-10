from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = {'example.com', 'test.com'}
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {"error": "Host not allowed"}