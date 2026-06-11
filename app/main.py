from fastapi import FastAPI
import subprocess
global_result = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        global_result = result.stdout
    except subprocess.CalledProcessError as e:
        global_result = str(e)
    return {"status": "completed", "result": global_result}