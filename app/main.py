from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host"}
    result = safe_ping(host)
    return {"status": "completed", "output": result}
def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts