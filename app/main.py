from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with shlex.quote
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}