from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host parameter"}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
def validate_host(host):
    # Implement your validation logic here
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts or '.' in host