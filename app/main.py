from fastapi import FastAPI
import subprocess
import re
class HostValidator:
    ALLOWED_HOSTS = {'example.com', 'test.com'}

    @staticmethod
def is_valid_host(host):
        return host in HostValidator.ALLOWED_HOSTS

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not HostValidator.is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    # Safe implementation using subprocess.run without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}