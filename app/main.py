from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        # Validate the host input to prevent injection attacks
        if not validate_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hosts or use a whitelist
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts