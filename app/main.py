from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation using subprocess.run()
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": execute_ping(host)}