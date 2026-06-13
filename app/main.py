from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using check_output instead of call with shell=True
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "result": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it does not contain malicious input
    if not host.replace('.', '').isdigit():
        return {"status": "failed", "error": "Invalid host format"}
    return safe_ping(host)