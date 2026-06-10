from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Define a list of allowed hosts or patterns
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
            return {"status": "completed", "output": output.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": e.output.decode()}
    else:
        return {"status": "error", "message": "Invalid host"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple regex for demonstration purposes
        return {"status": "error", "message": "Invalid host"}
    return safe_ping(host)