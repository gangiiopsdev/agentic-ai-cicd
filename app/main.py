from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "result": result}