from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_ping(host)
        return {"status": "completed"}
    else:
        raise HTTPException(status_code=400, detail="Invalid host")

def validate_host(host: str) -> bool:
    # Add your validation logic here
    return True