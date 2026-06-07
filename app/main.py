from fastapi import FastAPI
import subprocess
cimport = subprocess.check_output
call = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    try:
        call(['ping', host])
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}