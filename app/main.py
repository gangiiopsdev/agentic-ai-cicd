from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    try:
        # Use shlex.quote to safely escape the host argument
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping_with_validation(host):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    return safe_ping(host)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping_with_validation(host)
    return {"status": "completed", "result": result}