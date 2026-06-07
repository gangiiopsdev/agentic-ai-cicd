from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not validate_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
def validate_host(host: str) -> bool:
    # Implement a validation function to ensure the host is safe
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts