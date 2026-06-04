from fastapi import FastAPI, HTTPException
import subprocess
def validate_host(host: str) -> bool:
    return host.isnumeric() and len(host) == 3

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host format")
    command = ['ping', subprocess.check_output(['echo', host], text=True)]  # Sanitize input by echoing it
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "completed", "output": result.stdout}