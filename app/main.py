from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

async def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', subprocess.check_output(['nslookup', host]).decode().split()[4].strip()], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', subprocess.check_output(['nslookup', host]).decode().split()[4].strip()], check=True)