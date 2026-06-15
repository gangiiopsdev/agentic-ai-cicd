from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output to avoid shell=True
    try:
        result = subprocess.check_output(['ping', host], universal_newlines=True)
        return {"status": "completed", "result": result}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}