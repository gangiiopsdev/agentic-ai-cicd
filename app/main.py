from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it's a safe hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname or IP address")
    safe_ping(host)
    return {"status": "completed"}