from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    safe_host = host.strip()
    try:
        subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={"status": "completed"}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)