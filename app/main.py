from fastapi import FastAPI
import subprocess
call = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    result = call.stdout if call.returncode == 0 else 'Ping failed'
    return {"status": result}