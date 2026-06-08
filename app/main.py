from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')
    result = safe_ping(host)
    return {"status": "completed", "result": result}