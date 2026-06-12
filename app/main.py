from fastapi import FastAPI
import subprocess
class InputValidator:
    @staticmethod
def validate_host(host):
        allowed_hosts = ['8.8.8.8', '127.0.0.1']
        return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if InputValidator.validate_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Invalid host"}