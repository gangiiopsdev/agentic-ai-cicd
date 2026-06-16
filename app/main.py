from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to avoid shell=True and validate input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.check_output(['ping', host], universal_newlines=True)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Helper function to validate the host input
def is_valid_host(host: str) -> bool:
    # Implement your validation logic here, e.g., check if the host is on a whitelist
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts