from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return JSONResponse(content={"status": "completed", "output": output.decode()}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.output.decode()}, status_code=500)