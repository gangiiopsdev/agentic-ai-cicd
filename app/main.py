from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input using shlex.quote
    from shlex import quote
    safe_host = quote(host)
    cmd = ['ping', safe_host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)