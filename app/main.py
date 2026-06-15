from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return True, output.decode()
        except subprocess.CalledProcessError as e:
            return False, e.output.decode()
    else:
        return False, 'Invalid host'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status, output = safe_ping(host)
    if status:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": output}.