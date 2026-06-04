from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return False
    # Use a whitelist of allowed hosts or use a safer method like os.popen
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
        return True
    else:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid host parameter"}