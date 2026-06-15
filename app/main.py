from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid shell=True for security reasons
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout if result.returncode == 0 else None
def safe_ping_with_validation(host):
    # Validate input to prevent command injection
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return safe_ping(host)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Call the safe version of ping function with validation
    try:
        status = safe_ping_with_validation(host)
    except ValueError as e:
        return {"status": "error", "output": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": status}