from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    cmd = ['ping', host]
    return subprocess.run(cmd, check=True)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Sanitize input to prevent injection attacks
    safe_host = subprocess.quote(host, safe='')
    try:
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "returncode": result.returncode, "stdout": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "returncode": e.returncode, "stderr": e.stderr}