from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"status": "error", "message": "Invalid host input"}
    try:
        response = run_ping(host)
        return {"status": "completed", "output": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}