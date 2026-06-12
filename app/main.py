from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}