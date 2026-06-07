from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Simple validation, adjust based on your requirements
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts