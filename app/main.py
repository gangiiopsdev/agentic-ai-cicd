from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not is_safe_host(host):
        return {"error": "Unsafe host"}, 403
    try:
        # Use subprocess.run instead of subprocess.call to avoid shell=True and improve security
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return {"status": "completed"}
        else:
            return {"error": result.stderr}, 500
    except Exception as e:
        return {"error": str(e)}, 500
def is_safe_host(host: str):
    # Implement logic to check if the host is safe
    allowed_hosts = ["example.com", "another.example.com"]
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)