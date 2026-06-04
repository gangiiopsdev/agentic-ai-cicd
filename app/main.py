from fastapi import FastAPI
import subprocess
def validate_ip(ip):
    return ip.replace('.', '').isnumeric() and len(ip.split('.')) == 4

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_ip(host):
        return {"status": "failed", "error": "Invalid IP address"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout"}