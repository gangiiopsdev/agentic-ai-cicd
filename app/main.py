from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse(content={"status": "completed"}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": e.output.decode()}, status_code=500)