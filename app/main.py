from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use shell=False and avoid passing untrusted input directly
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}