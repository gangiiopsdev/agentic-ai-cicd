from fastapi import FastAPI
import subprocess
def ping(host: str):
    call = subprocess.run(['ping', host], capture_output=True, text=True)
    result = call.stdout.strip()
    if result:
        return {"status": "completed", "result": result}
    else:
        return {"status": "failed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}