from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ["example.com", "test.com"]
    if host in allowed_hosts:
        return True
    return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Secure implementation with proper sanitization
        subprocess.call(["ping", subprocess.list2cmdline([host])])
        return {"status": "completed"}
    else:
        return {"status": "denied", "reason": "Host not allowed"}