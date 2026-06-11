from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError("Invalid hostname")
    safe_host = subprocess.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 400

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)