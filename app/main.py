from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or '@' in host or not re.match(r'^[a-zA-Z0-9.-]+$', host): 
        raise ValueError('Invalid host input')
    args = ['ping', '-c', '1', subprocess.check_output(host).decode()]  # Use check_output to sanitize the host
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except ValueError as e:
        return {"error": str(e)}