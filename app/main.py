from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return True, output.decode()
        except subprocess.CalledProcessError as e:
            return False, e.output.decode()
    else:
        return False, 'Unauthorized host'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    is_safe, output = safe_ping(host)
    if is_safe:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}